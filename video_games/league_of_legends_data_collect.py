import requests
import json
import csv

### Variable 'a' is a dictionary of champion IDs matched with attributes- the Static API seems to be broken from the outside so I've called it 
### from the developer portal and copy/pasted it below for reference:

b= a['data']
champ_dict = {}
for key,value in b.iteritems():
	champ_dict[key] = value['name']
	
files_list = ['matches1.json', 'matches2.json', 'matches3.json', 'matches4.json', 'matches5.json', 'matches6.json', 'matches7.json', 'matches8.json', 'matches9.json', 'matches10.json']

####One could use the Riotgames API instead of pre-downloaded games but the rate limiting is relatively compared to most API.
# key = XXXX-XXXX-XXXX-XXXX-XXXX
# call =  'https://na1.api.riotgames.com/lol/match/v3/matches/' + match_id + '?api_key='
# in_str = requests.get(call2+key).content
# match_data = json.loads(in_str)
#### We also see that the process would be slow as each match would have to be called independently- no batching

for x in files_list:
	data = open(x).read()
	match_100 = json.loads(data, encoding = 'latin1')
	matches = match_100['matches']
	for match_data in matches:
		players = match_data['participants']
		p_d1 = {}
		p_d2 = {}
		for x in players:
			if x['teamId'] == 100:
				if str(x['timeline']['lane']) in p_d1.keys():
					p_d1[str(x['timeline']['lane']) + '2'] = champ_dict[str(x['championId'])]
				else:
					p_d1[x['timeline']['lane']] = champ_dict[str(x['championId'])]
			else:
				if x['timeline']['lane'] in p_d2.keys():
					p_d2[str(x['timeline']['lane']) + '2'] = champ_dict[str(x['championId'])]
				else:
					p_d2[x['timeline']['lane']] = champ_dict[str(x['championId'])]
		win = match_data['teams'][0]['win']
		try:
			row = [match_data['gameId'], p_d1['TOP'], p_d1['JUNGLE'], p_d1['MIDDLE'], p_d1['BOTTOM'], p_d1['BOTTOM2'], p_d2['TOP'], p_d2['JUNGLE'], p_d2['MIDDLE'], p_d2['BOTTOM'], p_d2['BOTTOM2'], win]
			with open("league_match_data.csv", "a") as fp:
				wr = csv.writer(fp, dialect='excel')
				wr.writerow(row)
		except KeyError:
			pass
	
### The static API doesn't seem to work by GET and returns 401 unauthorized regardless of key inclusion or not
### However, the execute on the Riot developers page works and I have copied and pasted here
### This is what would be returned without the starting defining of 'a' 

# a = {
#     "type": "champion",
#     "version": "7.21.1",
#     "data": {
#         "1": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 2,
#                 "defense": 3,
#                 "magic": 10
#             },
#             "title": "the Dark Child",
#             "id": 1,
#             "key": "Annie",
#             "name": "Annie"
#         },
#         "2": {
#             "info": {
#                 "difficulty": 3,
#                 "attack": 9,
#                 "defense": 5,
#                 "magic": 3
#             },
#             "title": "the Berserker",
#             "id": 2,
#             "key": "Olaf",
#             "name": "Olaf"
#         },
#         "3": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 1,
#                 "defense": 10,
#                 "magic": 6
#             },
#             "title": "the Colossus",
#             "id": 3,
#             "key": "Galio",
#             "name": "Galio"
#         },
#         "4": {
#             "info": {
#                 "difficulty": 9,
#                 "attack": 6,
#                 "defense": 2,
#                 "magic": 6
#             },
#             "title": "the Card Master",
#             "id": 4,
#             "key": "TwistedFate",
#             "name": "Twisted Fate"
#         },
#         "5": {
#             "info": {
#                 "difficulty": 2,
#                 "attack": 8,
#                 "defense": 6,
#                 "magic": 3
#             },
#             "title": "the Seneschal of Demacia",
#             "id": 5,
#             "key": "XinZhao",
#             "name": "Xin Zhao"
#         },
#         "6": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 8,
#                 "defense": 5,
#                 "magic": 3
#             },
#             "title": "the Dreadnought",
#             "id": 6,
#             "key": "Urgot",
#             "name": "Urgot"
#         },
#         "7": {
#             "info": {
#                 "difficulty": 9,
#                 "attack": 1,
#                 "defense": 4,
#                 "magic": 10
#             },
#             "title": "the Deceiver",
#             "id": 7,
#             "key": "Leblanc",
#             "name": "LeBlanc"
#         },
#         "8": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 2,
#                 "defense": 6,
#                 "magic": 8
#             },
#             "title": "the Crimson Reaper",
#             "id": 8,
#             "key": "Vladimir",
#             "name": "Vladimir"
#         },
#         "9": {
#             "info": {
#                 "difficulty": 9,
#                 "attack": 2,
#                 "defense": 3,
#                 "magic": 9
#             },
#             "title": "the Harbinger of Doom",
#             "id": 9,
#             "key": "Fiddlesticks",
#             "name": "Fiddlesticks"
#         },
#         "10": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 6,
#                 "defense": 6,
#                 "magic": 7
#             },
#             "title": "The Judicator",
#             "id": 10,
#             "key": "Kayle",
#             "name": "Kayle"
#         },
#         "11": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 10,
#                 "defense": 4,
#                 "magic": 2
#             },
#             "title": "the Wuju Bladesman",
#             "id": 11,
#             "key": "MasterYi",
#             "name": "Master Yi"
#         },
#         "12": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 6,
#                 "defense": 9,
#                 "magic": 5
#             },
#             "title": "the Minotaur",
#             "id": 12,
#             "key": "Alistar",
#             "name": "Alistar"
#         },
#         "13": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 2,
#                 "defense": 2,
#                 "magic": 10
#             },
#             "title": "the Rune Mage",
#             "id": 13,
#             "key": "Ryze",
#             "name": "Ryze"
#         },
#         "14": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 5,
#                 "defense": 9,
#                 "magic": 3
#             },
#             "title": "The Undead Juggernaut",
#             "id": 14,
#             "key": "Sion",
#             "name": "Sion"
#         },
#         "15": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 9,
#                 "defense": 3,
#                 "magic": 1
#             },
#             "title": "the Battle Mistress",
#             "id": 15,
#             "key": "Sivir",
#             "name": "Sivir"
#         },
#         "16": {
#             "info": {
#                 "difficulty": 3,
#                 "attack": 2,
#                 "defense": 5,
#                 "magic": 7
#             },
#             "title": "the Starchild",
#             "id": 16,
#             "key": "Soraka",
#             "name": "Soraka"
#         },
#         "17": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 5,
#                 "defense": 3,
#                 "magic": 7
#             },
#             "title": "the Swift Scout",
#             "id": 17,
#             "key": "Teemo",
#             "name": "Teemo"
#         },
#         "18": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 9,
#                 "defense": 3,
#                 "magic": 5
#             },
#             "title": "the Yordle Gunner",
#             "id": 18,
#             "key": "Tristana",
#             "name": "Tristana"
#         },
#         "19": {
#             "info": {
#                 "difficulty": 3,
#                 "attack": 9,
#                 "defense": 5,
#                 "magic": 3
#             },
#             "title": "the Uncaged Wrath of Zaun",
#             "id": 19,
#             "key": "Warwick",
#             "name": "Warwick"
#         },
#         "20": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 4,
#                 "defense": 6,
#                 "magic": 7
#             },
#             "title": "the Yeti Rider",
#             "id": 20,
#             "key": "Nunu",
#             "name": "Nunu"
#         },
#         "21": {
#             "info": {
#                 "difficulty": 1,
#                 "attack": 8,
#                 "defense": 2,
#                 "magic": 5
#             },
#             "title": "the Bounty Hunter",
#             "id": 21,
#             "key": "MissFortune",
#             "name": "Miss Fortune"
#         },
#         "22": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 7,
#                 "defense": 3,
#                 "magic": 2
#             },
#             "title": "the Frost Archer",
#             "id": 22,
#             "key": "Ashe",
#             "name": "Ashe"
#         },
#         "23": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 10,
#                 "defense": 5,
#                 "magic": 2
#             },
#             "title": "the Barbarian King",
#             "id": 23,
#             "key": "Tryndamere",
#             "name": "Tryndamere"
#         },
#         "24": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 7,
#                 "defense": 5,
#                 "magic": 7
#             },
#             "title": "Grandmaster at Arms",
#             "id": 24,
#             "key": "Jax",
#             "name": "Jax"
#         },
#         "25": {
#             "info": {
#                 "difficulty": 1,
#                 "attack": 1,
#                 "defense": 6,
#                 "magic": 8
#             },
#             "title": "Fallen Angel",
#             "id": 25,
#             "key": "Morgana",
#             "name": "Morgana"
#         },
#         "26": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 2,
#                 "defense": 5,
#                 "magic": 8
#             },
#             "title": "the Chronokeeper",
#             "id": 26,
#             "key": "Zilean",
#             "name": "Zilean"
#         },
#         "27": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 4,
#                 "defense": 8,
#                 "magic": 7
#             },
#             "title": "the Mad Chemist",
#             "id": 27,
#             "key": "Singed",
#             "name": "Singed"
#         },
#         "28": {
#             "info": {
#                 "difficulty": 10,
#                 "attack": 4,
#                 "defense": 2,
#                 "magic": 7
#             },
#             "title": "Agony's Embrace",
#             "id": 28,
#             "key": "Evelynn",
#             "name": "Evelynn"
#         },
#         "29": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 9,
#                 "defense": 2,
#                 "magic": 3
#             },
#             "title": "the Plague Rat",
#             "id": 29,
#             "key": "Twitch",
#             "name": "Twitch"
#         },
#         "30": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 2,
#                 "defense": 2,
#                 "magic": 10
#             },
#             "title": "the Deathsinger",
#             "id": 30,
#             "key": "Karthus",
#             "name": "Karthus"
#         },
#         "31": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 3,
#                 "defense": 7,
#                 "magic": 7
#             },
#             "title": "the Terror of the Void",
#             "id": 31,
#             "key": "Chogath",
#             "name": "Cho'Gath"
#         },
#         "32": {
#             "info": {
#                 "difficulty": 3,
#                 "attack": 2,
#                 "defense": 6,
#                 "magic": 8
#             },
#             "title": "the Sad Mummy",
#             "id": 32,
#             "key": "Amumu",
#             "name": "Amumu"
#         },
#         "33": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 4,
#                 "defense": 10,
#                 "magic": 5
#             },
#             "title": "the Armordillo",
#             "id": 33,
#             "key": "Rammus",
#             "name": "Rammus"
#         },
#         "34": {
#             "info": {
#                 "difficulty": 10,
#                 "attack": 1,
#                 "defense": 4,
#                 "magic": 10
#             },
#             "title": "the Cryophoenix",
#             "id": 34,
#             "key": "Anivia",
#             "name": "Anivia"
#         },
#         "35": {
#             "info": {
#                 "difficulty": 9,
#                 "attack": 8,
#                 "defense": 4,
#                 "magic": 6
#             },
#             "title": "the Demon Jester",
#             "id": 35,
#             "key": "Shaco",
#             "name": "Shaco"
#         },
#         "36": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 5,
#                 "defense": 7,
#                 "magic": 6
#             },
#             "title": "the Madman of Zaun",
#             "id": 36,
#             "key": "DrMundo",
#             "name": "Dr. Mundo"
#         },
#         "37": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 5,
#                 "defense": 2,
#                 "magic": 8
#             },
#             "title": "Maven of the Strings",
#             "id": 37,
#             "key": "Sona",
#             "name": "Sona"
#         },
#         "38": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 3,
#                 "defense": 5,
#                 "magic": 8
#             },
#             "title": "the Void Walker",
#             "id": 38,
#             "key": "Kassadin",
#             "name": "Kassadin"
#         },
#         "39": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 7,
#                 "defense": 4,
#                 "magic": 5
#             },
#             "title": "the Will of the Blades",
#             "id": 39,
#             "key": "Irelia",
#             "name": "Irelia"
#         },
#         "40": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 3,
#                 "defense": 5,
#                 "magic": 7
#             },
#             "title": "the Storm's Fury",
#             "id": 40,
#             "key": "Janna",
#             "name": "Janna"
#         },
#         "41": {
#             "info": {
#                 "difficulty": 9,
#                 "attack": 7,
#                 "defense": 6,
#                 "magic": 4
#             },
#             "title": "the Saltwater Scourge",
#             "id": 41,
#             "key": "Gangplank",
#             "name": "Gangplank"
#         },
#         "42": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 8,
#                 "defense": 3,
#                 "magic": 6
#             },
#             "title": "the Daring Bombardier",
#             "id": 42,
#             "key": "Corki",
#             "name": "Corki"
#         },
#         "43": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 1,
#                 "defense": 7,
#                 "magic": 8
#             },
#             "title": "the Enlightened One",
#             "id": 43,
#             "key": "Karma",
#             "name": "Karma"
#         },
#         "44": {
#             "info": {
#                 "difficulty": 3,
#                 "attack": 4,
#                 "defense": 8,
#                 "magic": 5
#             },
#             "title": "the Shield of Valoran",
#             "id": 44,
#             "key": "Taric",
#             "name": "Taric"
#         },
#         "45": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 2,
#                 "defense": 2,
#                 "magic": 10
#             },
#             "title": "the Tiny Master of Evil",
#             "id": 45,
#             "key": "Veigar",
#             "name": "Veigar"
#         },
#         "48": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 7,
#                 "defense": 6,
#                 "magic": 2
#             },
#             "title": "the Troll King",
#             "id": 48,
#             "key": "Trundle",
#             "name": "Trundle"
#         },
#         "50": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 2,
#                 "defense": 6,
#                 "magic": 9
#             },
#             "title": "the Master Tactician",
#             "id": 50,
#             "key": "Swain",
#             "name": "Swain"
#         },
#         "51": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 8,
#                 "defense": 2,
#                 "magic": 2
#             },
#             "title": "the Sheriff of Piltover",
#             "id": 51,
#             "key": "Caitlyn",
#             "name": "Caitlyn"
#         },
#         "53": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 4,
#                 "defense": 8,
#                 "magic": 5
#             },
#             "title": "the Great Steam Golem",
#             "id": 53,
#             "key": "Blitzcrank",
#             "name": "Blitzcrank"
#         },
#         "54": {
#             "info": {
#                 "difficulty": 2,
#                 "attack": 5,
#                 "defense": 9,
#                 "magic": 7
#             },
#             "title": "Shard of the Monolith",
#             "id": 54,
#             "key": "Malphite",
#             "name": "Malphite"
#         },
#         "55": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 4,
#                 "defense": 3,
#                 "magic": 9
#             },
#             "title": "the Sinister Blade",
#             "id": 55,
#             "key": "Katarina",
#             "name": "Katarina"
#         },
#         "56": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 9,
#                 "defense": 5,
#                 "magic": 2
#             },
#             "title": "the Eternal Nightmare",
#             "id": 56,
#             "key": "Nocturne",
#             "name": "Nocturne"
#         },
#         "57": {
#             "info": {
#                 "difficulty": 3,
#                 "attack": 3,
#                 "defense": 8,
#                 "magic": 6
#             },
#             "title": "the Twisted Treant",
#             "id": 57,
#             "key": "Maokai",
#             "name": "Maokai"
#         },
#         "58": {
#             "info": {
#                 "difficulty": 3,
#                 "attack": 8,
#                 "defense": 5,
#                 "magic": 2
#             },
#             "title": "the Butcher of the Sands",
#             "id": 58,
#             "key": "Renekton",
#             "name": "Renekton"
#         },
#         "59": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 6,
#                 "defense": 8,
#                 "magic": 3
#             },
#             "title": "the Exemplar of Demacia",
#             "id": 59,
#             "key": "JarvanIV",
#             "name": "Jarvan IV"
#         },
#         "60": {
#             "info": {
#                 "difficulty": 9,
#                 "attack": 6,
#                 "defense": 5,
#                 "magic": 7
#             },
#             "title": "the Spider Queen",
#             "id": 60,
#             "key": "Elise",
#             "name": "Elise"
#         },
#         "61": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 4,
#                 "defense": 3,
#                 "magic": 9
#             },
#             "title": "the Lady of Clockwork",
#             "id": 61,
#             "key": "Orianna",
#             "name": "Orianna"
#         },
#         "62": {
#             "info": {
#                 "difficulty": 3,
#                 "attack": 8,
#                 "defense": 5,
#                 "magic": 2
#             },
#             "title": "the Monkey King",
#             "id": 62,
#             "key": "MonkeyKing",
#             "name": "Wukong"
#         },
#         "63": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 2,
#                 "defense": 2,
#                 "magic": 9
#             },
#             "title": "the Burning Vengeance",
#             "id": 63,
#             "key": "Brand",
#             "name": "Brand"
#         },
#         "64": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 8,
#                 "defense": 5,
#                 "magic": 3
#             },
#             "title": "the Blind Monk",
#             "id": 64,
#             "key": "LeeSin",
#             "name": "Lee Sin"
#         },
#         "67": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 10,
#                 "defense": 1,
#                 "magic": 1
#             },
#             "title": "the Night Hunter",
#             "id": 67,
#             "key": "Vayne",
#             "name": "Vayne"
#         },
#         "68": {
#             "info": {
#                 "difficulty": 10,
#                 "attack": 3,
#                 "defense": 6,
#                 "magic": 8
#             },
#             "title": "the Mechanized Menace",
#             "id": 68,
#             "key": "Rumble",
#             "name": "Rumble"
#         },
#         "69": {
#             "info": {
#                 "difficulty": 10,
#                 "attack": 2,
#                 "defense": 3,
#                 "magic": 9
#             },
#             "title": "the Serpent's Embrace",
#             "id": 69,
#             "key": "Cassiopeia",
#             "name": "Cassiopeia"
#         },
#         "72": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 7,
#                 "defense": 6,
#                 "magic": 5
#             },
#             "title": "the Crystal Vanguard",
#             "id": 72,
#             "key": "Skarner",
#             "name": "Skarner"
#         },
#         "74": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 2,
#                 "defense": 6,
#                 "magic": 8
#             },
#             "title": "the Revered Inventor",
#             "id": 74,
#             "key": "Heimerdinger",
#             "name": "Heimerdinger"
#         },
#         "75": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 7,
#                 "defense": 5,
#                 "magic": 6
#             },
#             "title": "the Curator of the Sands",
#             "id": 75,
#             "key": "Nasus",
#             "name": "Nasus"
#         },
#         "76": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 5,
#                 "defense": 4,
#                 "magic": 7
#             },
#             "title": "the Bestial Huntress",
#             "id": 76,
#             "key": "Nidalee",
#             "name": "Nidalee"
#         },
#         "77": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 8,
#                 "defense": 7,
#                 "magic": 4
#             },
#             "title": "the Spirit Walker",
#             "id": 77,
#             "key": "Udyr",
#             "name": "Udyr"
#         },
#         "78": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 6,
#                 "defense": 7,
#                 "magic": 2
#             },
#             "title": "Keeper of the Hammer",
#             "id": 78,
#             "key": "Poppy",
#             "name": "Poppy"
#         },
#         "79": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 4,
#                 "defense": 7,
#                 "magic": 6
#             },
#             "title": "the Rabble Rouser",
#             "id": 79,
#             "key": "Gragas",
#             "name": "Gragas"
#         },
#         "80": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 9,
#                 "defense": 4,
#                 "magic": 3
#             },
#             "title": "the Artisan of War",
#             "id": 80,
#             "key": "Pantheon",
#             "name": "Pantheon"
#         },
#         "81": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 7,
#                 "defense": 2,
#                 "magic": 6
#             },
#             "title": "the Prodigal Explorer",
#             "id": 81,
#             "key": "Ezreal",
#             "name": "Ezreal"
#         },
#         "82": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 4,
#                 "defense": 6,
#                 "magic": 7
#             },
#             "title": "the Iron Revenant",
#             "id": 82,
#             "key": "Mordekaiser",
#             "name": "Mordekaiser"
#         },
#         "83": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 6,
#                 "defense": 6,
#                 "magic": 4
#             },
#             "title": "Shepherd of Souls",
#             "id": 83,
#             "key": "Yorick",
#             "name": "Yorick"
#         },
#         "84": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 5,
#                 "defense": 3,
#                 "magic": 8
#             },
#             "title": "the Fist of Shadow",
#             "id": 84,
#             "key": "Akali",
#             "name": "Akali"
#         },
#         "85": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 6,
#                 "defense": 4,
#                 "magic": 7
#             },
#             "title": "the Heart of the Tempest",
#             "id": 85,
#             "key": "Kennen",
#             "name": "Kennen"
#         },
#         "86": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 7,
#                 "defense": 7,
#                 "magic": 1
#             },
#             "title": "The Might of Demacia",
#             "id": 86,
#             "key": "Garen",
#             "name": "Garen"
#         },
#         "89": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 4,
#                 "defense": 8,
#                 "magic": 3
#             },
#             "title": "the Radiant Dawn",
#             "id": 89,
#             "key": "Leona",
#             "name": "Leona"
#         },
#         "90": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 2,
#                 "defense": 2,
#                 "magic": 9
#             },
#             "title": "the Prophet of the Void",
#             "id": 90,
#             "key": "Malzahar",
#             "name": "Malzahar"
#         },
#         "91": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 9,
#                 "defense": 3,
#                 "magic": 1
#             },
#             "title": "the Blade's Shadow",
#             "id": 91,
#             "key": "Talon",
#             "name": "Talon"
#         },
#         "92": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 8,
#                 "defense": 5,
#                 "magic": 1
#             },
#             "title": "the Exile",
#             "id": 92,
#             "key": "Riven",
#             "name": "Riven"
#         },
#         "96": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 8,
#                 "defense": 2,
#                 "magic": 5
#             },
#             "title": "the Mouth of the Abyss",
#             "id": 96,
#             "key": "KogMaw",
#             "name": "Kog'Maw"
#         },
#         "98": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 3,
#                 "defense": 9,
#                 "magic": 3
#             },
#             "title": "the Eye of Twilight",
#             "id": 98,
#             "key": "Shen",
#             "name": "Shen"
#         },
#         "99": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 2,
#                 "defense": 4,
#                 "magic": 9
#             },
#             "title": "the Lady of Luminosity",
#             "id": 99,
#             "key": "Lux",
#             "name": "Lux"
#         },
#         "101": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 1,
#                 "defense": 3,
#                 "magic": 10
#             },
#             "title": "the Magus Ascendant",
#             "id": 101,
#             "key": "Xerath",
#             "name": "Xerath"
#         },
#         "102": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 8,
#                 "defense": 6,
#                 "magic": 3
#             },
#             "title": "the Half-Dragon",
#             "id": 102,
#             "key": "Shyvana",
#             "name": "Shyvana"
#         },
#         "103": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 3,
#                 "defense": 4,
#                 "magic": 8
#             },
#             "title": "the Nine-Tailed Fox",
#             "id": 103,
#             "key": "Ahri",
#             "name": "Ahri"
#         },
#         "104": {
#             "info": {
#                 "difficulty": 3,
#                 "attack": 8,
#                 "defense": 5,
#                 "magic": 3
#             },
#             "title": "the Outlaw",
#             "id": 104,
#             "key": "Graves",
#             "name": "Graves"
#         },
#         "105": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 6,
#                 "defense": 4,
#                 "magic": 7
#             },
#             "title": "the Tidal Trickster",
#             "id": 105,
#             "key": "Fizz",
#             "name": "Fizz"
#         },
#         "106": {
#             "info": {
#                 "difficulty": 3,
#                 "attack": 7,
#                 "defense": 7,
#                 "magic": 4
#             },
#             "title": "the Thunder's Roar",
#             "id": 106,
#             "key": "Volibear",
#             "name": "Volibear"
#         },
#         "107": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 7,
#                 "defense": 4,
#                 "magic": 2
#             },
#             "title": "the Pridestalker",
#             "id": 107,
#             "key": "Rengar",
#             "name": "Rengar"
#         },
#         "110": {
#             "info": {
#                 "difficulty": 2,
#                 "attack": 7,
#                 "defense": 3,
#                 "magic": 4
#             },
#             "title": "the Arrow of Retribution",
#             "id": 110,
#             "key": "Varus",
#             "name": "Varus"
#         },
#         "111": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 4,
#                 "defense": 6,
#                 "magic": 6
#             },
#             "title": "the Titan of the Depths",
#             "id": 111,
#             "key": "Nautilus",
#             "name": "Nautilus"
#         },
#         "112": {
#             "info": {
#                 "difficulty": 9,
#                 "attack": 2,
#                 "defense": 4,
#                 "magic": 10
#             },
#             "title": "the Machine Herald",
#             "id": 112,
#             "key": "Viktor",
#             "name": "Viktor"
#         },
#         "113": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 5,
#                 "defense": 7,
#                 "magic": 6
#             },
#             "title": "Fury of the North",
#             "id": 113,
#             "key": "Sejuani",
#             "name": "Sejuani"
#         },
#         "114": {
#             "info": {
#                 "difficulty": 3,
#                 "attack": 10,
#                 "defense": 4,
#                 "magic": 2
#             },
#             "title": "the Grand Duelist",
#             "id": 114,
#             "key": "Fiora",
#             "name": "Fiora"
#         },
#         "115": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 2,
#                 "defense": 4,
#                 "magic": 9
#             },
#             "title": "the Hexplosives Expert",
#             "id": 115,
#             "key": "Ziggs",
#             "name": "Ziggs"
#         },
#         "117": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 4,
#                 "defense": 5,
#                 "magic": 7
#             },
#             "title": "the Fae Sorceress",
#             "id": 117,
#             "key": "Lulu",
#             "name": "Lulu"
#         },
#         "119": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 9,
#                 "defense": 3,
#                 "magic": 1
#             },
#             "title": "the Glorious Executioner",
#             "id": 119,
#             "key": "Draven",
#             "name": "Draven"
#         },
#         "120": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 8,
#                 "defense": 6,
#                 "magic": 4
#             },
#             "title": "the Shadow of War",
#             "id": 120,
#             "key": "Hecarim",
#             "name": "Hecarim"
#         },
#         "121": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 9,
#                 "defense": 4,
#                 "magic": 3
#             },
#             "title": "the Voidreaver",
#             "id": 121,
#             "key": "Khazix",
#             "name": "Kha'Zix"
#         },
#         "122": {
#             "info": {
#                 "difficulty": 2,
#                 "attack": 9,
#                 "defense": 5,
#                 "magic": 1
#             },
#             "title": "the Hand of Noxus",
#             "id": 122,
#             "key": "Darius",
#             "name": "Darius"
#         },
#         "126": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 8,
#                 "defense": 4,
#                 "magic": 3
#             },
#             "title": "the Defender of Tomorrow",
#             "id": 126,
#             "key": "Jayce",
#             "name": "Jayce"
#         },
#         "127": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 2,
#                 "defense": 5,
#                 "magic": 8
#             },
#             "title": "the Ice Witch",
#             "id": 127,
#             "key": "Lissandra",
#             "name": "Lissandra"
#         },
#         "131": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 7,
#                 "defense": 6,
#                 "magic": 8
#             },
#             "title": "Scorn of the Moon",
#             "id": 131,
#             "key": "Diana",
#             "name": "Diana"
#         },
#         "133": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 9,
#                 "defense": 4,
#                 "magic": 2
#             },
#             "title": "Demacia's Wings",
#             "id": 133,
#             "key": "Quinn",
#             "name": "Quinn"
#         },
#         "134": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 2,
#                 "defense": 3,
#                 "magic": 9
#             },
#             "title": "the Dark Sovereign",
#             "id": 134,
#             "key": "Syndra",
#             "name": "Syndra"
#         },
#         "136": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 2,
#                 "defense": 3,
#                 "magic": 8
#             },
#             "title": "The Star Forger",
#             "id": 136,
#             "key": "AurelionSol",
#             "name": "Aurelion Sol"
#         },
#         "141": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 10,
#                 "defense": 6,
#                 "magic": 1
#             },
#             "title": "the Shadow Reaper",
#             "id": 141,
#             "key": "Kayn",
#             "name": "Kayn"
#         },
#         "143": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 4,
#                 "defense": 3,
#                 "magic": 8
#             },
#             "title": "Rise of the Thorns",
#             "id": 143,
#             "key": "Zyra",
#             "name": "Zyra"
#         },
#         "150": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 6,
#                 "defense": 5,
#                 "magic": 5
#             },
#             "title": "the Missing Link",
#             "id": 150,
#             "key": "Gnar",
#             "name": "Gnar"
#         },
#         "154": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 3,
#                 "defense": 7,
#                 "magic": 7
#             },
#             "title": "the Secret Weapon",
#             "id": 154,
#             "key": "Zac",
#             "name": "Zac"
#         },
#         "157": {
#             "info": {
#                 "difficulty": 10,
#                 "attack": 8,
#                 "defense": 4,
#                 "magic": 4
#             },
#             "title": "the Unforgiven",
#             "id": 157,
#             "key": "Yasuo",
#             "name": "Yasuo"
#         },
#         "161": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 2,
#                 "defense": 2,
#                 "magic": 10
#             },
#             "title": "the Eye of the Void",
#             "id": 161,
#             "key": "Velkoz",
#             "name": "Vel'Koz"
#         },
#         "163": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 1,
#                 "defense": 7,
#                 "magic": 8
#             },
#             "title": "the Stoneweaver",
#             "id": 163,
#             "key": "Taliyah",
#             "name": "Taliyah"
#         },
#         "164": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 8,
#                 "defense": 6,
#                 "magic": 3
#             },
#             "title": "the Steel Shadow",
#             "id": 164,
#             "key": "Camille",
#             "name": "Camille"
#         },
#         "201": {
#             "info": {
#                 "difficulty": 3,
#                 "attack": 3,
#                 "defense": 9,
#                 "magic": 4
#             },
#             "title": "the Heart of the Freljord",
#             "id": 201,
#             "key": "Braum",
#             "name": "Braum"
#         },
#         "202": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 10,
#                 "defense": 2,
#                 "magic": 6
#             },
#             "title": "the Virtuoso",
#             "id": 202,
#             "key": "Jhin",
#             "name": "Jhin"
#         },
#         "203": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 8,
#                 "defense": 2,
#                 "magic": 2
#             },
#             "title": "The Eternal Hunters",
#             "id": 203,
#             "key": "Kindred",
#             "name": "Kindred"
#         },
#         "222": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 9,
#                 "defense": 2,
#                 "magic": 4
#             },
#             "title": "the Loose Cannon",
#             "id": 222,
#             "key": "Jinx",
#             "name": "Jinx"
#         },
#         "223": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 3,
#                 "defense": 9,
#                 "magic": 6
#             },
#             "title": "the River King",
#             "id": 223,
#             "key": "TahmKench",
#             "name": "Tahm Kench"
#         },
#         "236": {
#             "info": {
#                 "difficulty": 6,
#                 "attack": 8,
#                 "defense": 5,
#                 "magic": 3
#             },
#             "title": "the Purifier",
#             "id": 236,
#             "key": "Lucian",
#             "name": "Lucian"
#         },
#         "238": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 9,
#                 "defense": 2,
#                 "magic": 1
#             },
#             "title": "the Master of Shadows",
#             "id": 238,
#             "key": "Zed",
#             "name": "Zed"
#         },
#         "240": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 8,
#                 "defense": 2,
#                 "magic": 2
#             },
#             "title": "the Cantankerous Cavalier",
#             "id": 240,
#             "key": "Kled",
#             "name": "Kled"
#         },
#         "245": {
#             "info": {
#                 "difficulty": 8,
#                 "attack": 5,
#                 "defense": 3,
#                 "magic": 7
#             },
#             "title": "the Boy Who Shattered Time",
#             "id": 245,
#             "key": "Ekko",
#             "name": "Ekko"
#         },
#         "254": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 8,
#                 "defense": 5,
#                 "magic": 3
#             },
#             "title": "the Piltover Enforcer",
#             "id": 254,
#             "key": "Vi",
#             "name": "Vi"
#         },
#         "266": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 8,
#                 "defense": 4,
#                 "magic": 3
#             },
#             "title": "the Darkin Blade",
#             "id": 266,
#             "key": "Aatrox",
#             "name": "Aatrox"
#         },
#         "267": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 4,
#                 "defense": 3,
#                 "magic": 7
#             },
#             "title": "the Tidecaller",
#             "id": 267,
#             "key": "Nami",
#             "name": "Nami"
#         },
#         "268": {
#             "info": {
#                 "difficulty": 9,
#                 "attack": 6,
#                 "defense": 3,
#                 "magic": 8
#             },
#             "title": "the Emperor of the Sands",
#             "id": 268,
#             "key": "Azir",
#             "name": "Azir"
#         },
#         "412": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 5,
#                 "defense": 6,
#                 "magic": 6
#             },
#             "title": "the Chain Warden",
#             "id": 412,
#             "key": "Thresh",
#             "name": "Thresh"
#         },
#         "420": {
#             "info": {
#                 "difficulty": 4,
#                 "attack": 8,
#                 "defense": 6,
#                 "magic": 3
#             },
#             "title": "the Kraken Priestess",
#             "id": 420,
#             "key": "Illaoi",
#             "name": "Illaoi"
#         },
#         "421": {
#             "info": {
#                 "difficulty": 3,
#                 "attack": 8,
#                 "defense": 5,
#                 "magic": 2
#             },
#             "title": "the Void Burrower",
#             "id": 421,
#             "key": "RekSai",
#             "name": "Rek'Sai"
#         },
#         "427": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 3,
#                 "defense": 5,
#                 "magic": 7
#             },
#             "title": "the Green Father",
#             "id": 427,
#             "key": "Ivern",
#             "name": "Ivern"
#         },
#         "429": {
#             "info": {
#                 "difficulty": 7,
#                 "attack": 8,
#                 "defense": 2,
#                 "magic": 4
#             },
#             "title": "the Spear of Vengeance",
#             "id": 429,
#             "key": "Kalista",
#             "name": "Kalista"
#         },
#         "432": {
#             "info": {
#                 "difficulty": 9,
#                 "attack": 4,
#                 "defense": 4,
#                 "magic": 5
#             },
#             "title": "the Wandering Caretaker",
#             "id": 432,
#             "key": "Bard",
#             "name": "Bard"
#         },
#         "497": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 2,
#                 "defense": 4,
#                 "magic": 8
#             },
#             "title": "The Charmer",
#             "id": 497,
#             "key": "Rakan",
#             "name": "Rakan"
#         },
#         "498": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 10,
#                 "defense": 6,
#                 "magic": 1
#             },
#             "title": "the Rebel",
#             "id": 498,
#             "key": "Xayah",
#             "name": "Xayah"
#         },
#         "516": {
#             "info": {
#                 "difficulty": 5,
#                 "attack": 5,
#                 "defense": 9,
#                 "magic": 3
#             },
#             "title": "The Fire below the Mountain",
#             "id": 516,
#             "key": "Ornn",
#             "name": "Ornn"
#         }
#     }
# }
	
	
