### K-Means Unsupervised Learning for identifying 'types' of artists
### Visualization only in 2D



###artist_dict from webscraping app
artist_dict = {}
music_df = pd.DataFrame(artist_dict)
music_df2 = music_df.transpose()
colnames = ['Spotify_Followers', 'Facebook_Fan_Count', 'YouTube_Subscribers', 'Soundcloud_Followers']
music_df2.columns = colnames

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


X = music_df2
clf = KMeans(n_clusters = 3)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_
colors = ["g.", "r.", "c.", "b.", "k.", "o."]

labels = clf.predict(X)
artists_names = list(music_df.columns)



clusters = {}
n = 0
for item in labels:
	if item in clusters:
		clusters[item].append(artists_names[n])
	else:
		clusters[item] = [artists_names[n]]
	n +=1
	
clusters[0][:30]	
clusters[1][:30]	
clusters[2][:30]	
for i in range(len(X)):
	plt.plot(X.iloc[i][0], X.iloc[i][3], colors[labels[i]], markersize = 10)
plt.scatter(centroids[:,0], centroids[:1], marker='x', size=150, linewidths=5)
plt.show()

for i in range(len(X)):
	plt.plot(X.iloc[i][0], X.iloc[i][2], colors[labels[i]], markersize = 10)
plt.scatter(centroids[:,0], centroids[:1], marker='x', size=150, linewidths=5)
plt.show()

for i in range(len(X)):
	plt.plot(X.iloc[i][2], X.iloc[i][3], colors[labels[i]], markersize = 10)
plt.scatter(centroids[:,0], centroids[:1], marker='x', size=150, linewidths=5)
plt.show()

######FINDINGS

###clusters[0][:30]
###['21_savage', '2_chainz', '2cellos', '30_seconds_to_mars', '3_doors_down', '3oh!3', '6lack', '99_percent', '@iheartmemphis',
###'a$ap_ferg', 'a$ap_rocky', 'a_boogie_wit_da_hoodie', 'a_rocket_to_the_moon', 'a_thousand_horses', 'a_tribe_called_quest',
###'aaliyah', 'aaron_lewis', 'ace_hood', 'action_bronson', 'adam_hicks', 'adam_lambert', 'adam_wakefield', 'agatha_lee_monn',
###'ajr', 'alabama', 'alabama_shakes', 'alan_jackson', 'alan_walker', 'alessia_cara', 'alesso']
###clusters[1][:30]
###['50_cent', 'adele', 'akon', 'ariana_grande', 'avril_lavigne', 'beyonce', 'britney_spears', 'bruno_mars', 
###'chris_brown', 'coldplay', 'david_guetta', 'demi_lovato', 'drake', 'dwayne_johnson', 'eminem', 'enrique_iglesias', 
###'jennifer_lopez', 'justin_bieber', 'justin_timberlake', 'katy_perry', 'lady_gaga', 'lil_wayne', 'linkin_park', 
###'maroon_5', 'michael_jackson', 'miley_cyrus', 'nicki_minaj', 'one_direction', 'pitbull', 'rihanna']

###clusters[2][:30]
###['5_seconds_of_summer', 'acdc', 'adam_levine', 'aerosmith', 'afrojack', 'alicia_keys', 'amy_winehouse', 'armin_van_buuren',
###'austin_mahone', 'avenged_sevenfold', 'avicii', 'backstreet_boys', 'bella_thorne', 'big_bang', 'big_time_rush', 
###'black_sabbath', 'blake_shelton', 'blink_182', 'bon_jovi', 'calvin_harris', 'cam', 'carly_rae_jepsen', 
###'carrie_underwood', 'christina_aguilera', 'ciara', 'claudia_leitte', 'daddy_yankee', 'daft_punk', 'deadmau5',
###'disturbed']
