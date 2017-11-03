#Linear Model in R

Stats <- read.csv("league_match_data.csv")
str(Stats)

#Uses interaction variables of every participant combination as well as independent contribution

summary(lm(Stats$win ~ Stats$T1_Top*Stats$T1_Jun*Stats$T1_Mid*Stats$T1_Bot*Stats$T1_Bot*Stats$T2_Top*Stats$T2_Jun*Stats$T2_Mid*Stats$T2_Bot*Stats$T2_Bot))
