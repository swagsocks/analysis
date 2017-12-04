library(httr)
library(jsonlite)

#Soundcloud API
client_id <- "BQiQ6t40b0CG4GgDnZdjyctLNVyMNMlO"
client_key <- "Bf4XvY4dFQyWmJ7PqubEunZuGZGDcweq"
token <- c(client_id, client_key)
url <- "https://api.soundcloud.com/tracks?client_id=BQiQ6t40b0CG4GgDnZdjyctLNVyMNMlO"

req <- GET(url, 
           authenticate(client_id, client_key)) 
raw.results <- content(req)

#Facebook
library(Rfacebook)
library(xml2)

#Oauth
tokenFB<-    fbOAuth(app_id = "133238567175116", app_secret = "0146d3185da1cdfe34316272d41ed97e", 
                     extended_permissions = FALSE, legacy_permissions = FALSE)
fb <- callAPI("facebook.com/cameron.holl", tokenFB) 
tokenFB


#Stalker Function
Pricer <- function(soundcloud, hypehype, FBFB, YT, spot, FM) 
{
    #Stanaj - Plug in username after users
    
    pompei<- content(GET(paste0("https://api.soundcloud.com/users/?q=",soundcloud,"&types=people&client_id=BQiQ6t40b0CG4GgDnZdjyctLNVyMNMlO")))
    SoundCloudFollowers <- pompei[[1]]$followers_count

    
    #FUCK YEAH
    
    #Hypem - plug in name after artists
    url2<- paste0("https://api.hypem.com/v2/artists/",hypehype,"/tracks?key=swagger")
    hypem <- GET(url2)
    raw.results2 <- content(hypem)
    
    Hype <- lapply(raw.results2, function(x) {
        names(x) <- (1:length(x))
        
        loved <- x$"9"
        blogs <- x$"10"
        HypemData <- data.frame(loved, blogs)
    })
    
    HypeEm <- do.call("rbind", Hype)
    HypemLoved <- sum(HypeEm$loved)
    HypemBlogged <- sum(HypeEm$blogs)

    
    #FaceBook API Call - plug in name after v2.8/
    
    
    pig<-  content(GET(paste0("https://graph.facebook.com/v2.8/search?q=",FBFB,"&type=page"), tokenFB))
   
    pablo<- pig$data[[1]]$id
    
    
    me<- paste0("https://graph.facebook.com/v2.8/",pablo,"/?fields=id,name,fan_count,talking_about_count")
    getme<- GET(me, tokenFB)
    FBdata <- content(getme)


    #YouTube 
    
    
    #video
    #find id: https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.search.list?part=id&q=stanaj&_h=1&
    #match statistics with appropriate youtube channel
    
    
    
    #YouTube channel
    url0 <- paste0("https://www.googleapis.com/youtube/v3/search?part=id&q=",YT,"&key=AIzaSyCoVnJo82iHumeaONcM7m8XLtUoQdaZkJQ")
    
    Tuber <- GET(url0)
    
    
    apple <- content(Tuber)
    apple1 <- (apple$items)
    apple2<-lapply(apple1, function(x) {
        
        (x$id$channelId)
        
    })
   
    

    if (!is.null(unlist(apple2))){
        orange<- head(na.omit(unlist(apple2)),1)
        url2 <- paste0("https://www.googleapis.com/youtube/v3/channels?id=",orange,"&key=AIzaSyCoVnJo82iHumeaONcM7m8XLtUoQdaZkJQ&part=statistics")
        
        YouTube <- GET(url2)
        contentYT<- content(YouTube)
        names(contentYT$items) <- "more" 
        YouTubeStat <- contentYT$items$more$statistics
        YouTubeViews <- YouTubeStat$viewCount
        YouTubeComments <- YouTubeStat$commentCount
        YouTubeSubs <- YouTubeStat$subscriberCount
        YouTubeHiddenSubs <- YouTubeStat$hiddenSubscriberCount
        YouTubeVideoCount <- YouTubeStat$videoCount
    }
    
    if (is.null(unlist(apple2))){
        YouTubeViews <- NA
        YouTubeComments <- NA
        YouTubeSubs <- NA
        YouTubeHiddenSubs <- NA
        YouTubeVideoCount <- NA
    }

    
    #Spotify
    #Search spotify and artist name in google. ID in URL
    
    
    pickle<- content(GET(paste0("https://api.spotify.com/v1/search?q=",spot,"&type=artist")))
    if (!is.null(unlist(pickle$artists$items[1]))) {
        pickle1<- pickle$artists$items[1]
        SpotifyFollowers <- pickle1[[1]]$followers$total
        SpotifyPopularity <- pickle1[[1]]$popularity
    }
    if (is.null(unlist(pickle$artists$items[1]))) {
        SpotifyFollowers <- NA
        SpotifyPopularity <- NA
    }
    
    #HideYoKids
    
    #Last FM  Reenter Artist name in Artist = ... 
    LFMurl <- paste0("http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=",FM,"&api_key=5f55a85aa60557340b3db731d358d1a2&format=json")
    LastFMraw <- GET(LFMurl)
    LastFM <- content(LastFMraw)
    LastFMStats <- LastFM$artist$stats
    
   

    #Easy Money
    Date <- as.character(Sys.Date())
    Collected <- data.frame(Date, SoundCloudFollowers, HypemLoved, HypemBlogged, FBdata, YouTubeViews,
                            YouTubeComments, YouTubeSubs, YouTubeHiddenSubs, YouTubeVideoCount,  SpotifyFollowers, SpotifyPopularity, LastFMStats)

     
    names <- c("Date", "SoundCloudFollowers", "HypemLoved", "HypemBlogged", 
               "fbID", "fbName", "fbFans", "fbTalkingAbout", "YouTubeViews", "YouTubeComments", "YouTubeSubs", 
               "YouTubeHiddenSubs", "YouTubeVideoCount", "SpotifyFollowers", "SpotifyPopularity", "LastFMListeners", "LastFMplays")
    names(Collected) <- names
    print(Collected)
}

DJDJ<- read.csv("data3.csv")
names(DJDJ) <- c("Dj.Names", "Avg.Tickets.Sold", "Avg.Gross", "Ticket.Price")
DJprices <- DJDJ
DjNames<- DJprices$Dj.Names

DJlist<- lapply(DjNames, as.character)


DJlist9<- lapply(DJlist, function(x) {
    x <- as.list(rep(x, 6))
   
})


Pricer1 <- function(Concert) {
    do.call(Pricer, Concert) 
}


ConcertPrice<- lapply(DJlist9, Pricer1)

WebScraper<- do.call("rbind", ConcertPrice)
PricingData<- data.frame(DJprices$Dj.Names, DJprices$Avg.Tickets.Sold, DJprices$Avg.Gross, DJprices$Ticket.Price)
DanceParty<- cbind(WebScraper, PricingData)



Pricer1(as.list(rep("g+dragon", 6)))
write.csv(DanceParty, "Dance.Party.Now.csv")

Stats <- read.csv("Dance.Party.Now.csv")
str(Stats)
Stats$DJprices.Avg.Gross <- as.numeric(as.character(Stats$DJprices.Avg.Gross))

summary(lm(Stats$DJprices.Avg.Gross ~ Stats$SpotifyFollowers + Stats$fbFans + Stats$LastFMplays +Stats$SoundCloudFollowers))
summary(lm(Stats$DJprices.Ticket.Price ~ Stats$SpotifyFollowers + Stats$fbFans + Stats$LastFMplays +Stats$HypemBlogged))
