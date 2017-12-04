library(Rfacebook)
library(xml2)
library(jsonlite)
library(httr)


AeroToken<- "EAACEdEose0cBAG8WiHfS2oWM84A3tGZAeejMQcvKkVjj2W17HuZBjCZCUgnEOUNnZBGgsncuVMn4KsLCE2ed8sotJBq1KInmiwlGlSiZBKXlBRtxgXmudvBoRox9SvSmNbee8h52E8zlZAcBtbzmeZCRiBl32xgGtyjYzoG4Ln8kYO2zMviSA5ZCzpOyZBXMuQy0ZD"

Last16<- content(GET(paste0("https://graph.facebook.com/v2.8/me?fields=posts&access_token=", AeroToken)))

Pages <- c(1:22)
Collect <- function(page) {
    IDs<- Last16$posts$data[[page]]$id
    }

PostIDs <- lapply(Pages, Collect)


#Post1
OneColumn<- function (postID) {
Post1 <- GET(paste0("https://graph.facebook.com/v2.8/",postID,"?fields=reactions.limit(3000)&access_token=", AeroToken))
Reactions1<- content(Post1)
Numbers <- c(1:3000)

if(length(Reactions1$reactions$data) >= 3000) 
{
Names <- function(index) {
Frame1 <- data.frame(Reactions1$reactions$data[[index]]$name)
    }
  
Column1 <- lapply(Numbers, Names)

Column.1<- do.call(rbind, Column1)
Column.1
}
else 
{print("Sheep")}
}

Query<- lapply(PostIDs, OneColumn)
table1<- do.call(cbind, Query)
names(table1)
table2 <- table1[ , -which(names(table1) %in% c("\"Sheep\""))]
table <- table2[, 1:16]


columns<- c("Post1", "Post2", "Post3", "Post4", "Post5", "Post6", "Post7", "Post8", 
            "Post9", "Post10", "Post11", "Post12", "Post13", "Post14", "Post15", "Post16")
names(table) <- columns
what <- c(1:16)
vectorize<- function(now) {
    as.character(table[[now]])
}

library(plyr)
mission<- lapply(what, vectorize)
TopFans<- count(unlist(mission))
names(TopFans) <- c("Fan", "freq")
tail(TopFans[order(TopFans$freq),], 100)
nrow(TopFans[TopFans$freq > 5,])
nrow(TopFans)
TopFans$freq

hist(TopFans$freq, breaks= 15)

couple1 <- as.character(na.omit(table$Match1))

four1<- couple1[match(couple1, couple2)]

four11<- as.character(na.omit(four1))

frame2<- as.character(na.omit(frame$Match))
frame2<- as.data.frame(frame2)
str(frame2)
frame3 <- apply(frame2, 2 ,sort, decreasing=F)
match(Column.2, Column.3)

