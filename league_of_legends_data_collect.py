import requests
import json
import csv

for match_id in matches:
	key = 'XXXX-XXXX-XXXX-XXXX-XXXX-XXXX'
	call2 = 'https://na1.api.riotgames.com/lol/match/v3/matches/' + match_id + '?api_key='
	in_str = requests.get(call2+key).content
	match_data = json.loads(in_str)
	players = match_data['participants']
	p_d1 = {}
	p_d2 = {}
	for x in players:
		x_raw = requests.get('https://na1.api.riotgames.com/lol/static-data/v3/champions/'
		 + str(x['championId'])
		 + '?locale=en_US&tags=info&api_key='
		 + key)
		x_info = json.loads(x_raw.content)
		if x['teamId'] == 100:
			p_d1[x['timeline']['lane']] = x_info['name']
		else:
			p_d2[x['timeline']['lane']] = x_info['name']
	win = match_data['teams']['win']
	row = [match_id, p_d1['top'], p_d1['jungle'], p_d1['mid'], p_d1['bottom'], p_d1['bottom'],
	p_d2['top'], p_d2['jungle'], p_d2['mid'], p_d2['bottom'], p_d2['bottom'], win]
	with open("league_match_data.csv", "a") as fp:
		wr = csv.writer(fp, dialect='excel')
		wr.writerow(row)

