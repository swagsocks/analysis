#Linear Model in R

Stats <- read.csv("league_match_data.csv")
str(Stats)

#Uses interaction variables of every participant combination as well as independent contribution

summary(lm(Stats$win ~ Stats$T1_Top*Stats$T1_Jun*Stats$T1_Mid*Stats$T1_Bot*Stats$T1_Bot*Stats$T2_Top*Stats$T2_Jun*Stats$T2_Mid*Stats$T2_Bot*Stats$T2_Bot))
### We find in theory this would work but even having the interaction variable between two positions requires tremendous computation
### (Imagine 30+ champions x 30+ champions)
### Thus this technique is inadequate to predict game results

###----------------------------------------------------------------------------



#Individual probabilities and Counter Probabilities in Python
import pandas as pd
df1 = pd.read_csv('league_match_data.csv')

df1.to_dict()

#We find most champions win around 50% of games
def independent(position, subject):
	position1 = 'T1_' + position
	df2 = df1.loc[lambda df: df.loc[ :, position1] == subject, :]
	df2_5 = df2.loc[lambda df: df.Win == 'Win', :]
	position2 = 'T2_' + position
	df3 = df1.loc[lambda df: df.loc[: , position2] == subject, :]
	df3_5 = df3.loc[lambda df: df.Win == 'Fail', :]
	result = (len(df3_5) + len(df2_5))/float(len(df3)+len(df2))
	return result

#We find that sometimes	the counter suggestions provided by Lol Counter do not match the data- this obvious is affected by the skill of the player relative to the champion
#I hypothesize those who main a champion are probably use to playing against their counters and thus develop skills to adequately mitigate the counter
#See Top Riven vs Darius- Darius should win by Lol Counter but has lost every matchup against Riven in 1000 games

def against(position, subject1, subject2):
	position1 = 'T1_' + position
	position2 = 'T2_' + position
	df2 = df1.loc[lambda df: df.loc[ :, position1] == subject1, :]
	df2_1 = df2.loc[lambda df: df.loc[:, position2] == subject2, :]
	df2_2 = df2_1.loc[lambda df: df.Win == 'Win', :]
	df3 = df1.loc[lambda df: df.loc[ :, position2] == subject1, :]
	df3_1 = df3.loc[lambda df: df.loc[:, position1] == subject2, :]
	df3_2 = df3_1.loc[lambda df: df.Win == 'Fail', :]
	result = (len(df3_2) + len(df2_2))/float(len(df3_1)+len(df2_1))
	print result


