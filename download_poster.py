'''
'Action', 'Adult', 'Adventure', 'Animation', 'Biography',
'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror',
'Music', 'Musical', 'Mystery', 'News', 'Reality-TV',
'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show',
'Thriller', 'War', 'Western'
총 28개
'''

import csv
import requests 

f = open('MovieGenre.csv', 'r', encoding="ISO-8859-1")
rdr = csv.reader(f)

for i, line in enumerate(rdr):
    if 0 <= i <= 32973:
        continue
    genre_vector = '0000000000000000000000000000'
    genre_vector = list(genre_vector)

    genre = line[1]
    genre = genre.split('|')

    for gen in genre:
        if gen == 'Action':
            genre_vector[0] = '1'
        elif gen == 'Adult':
            genre_vector[1] = '1'
        elif gen == 'Adventure':
            genre_vector[2] = '1'
        elif gen == 'Animation':
            genre_vector[3] = '1'
        elif gen == 'Biography':
            genre_vector[4] = '1'
        elif gen == 'Comedy':
            genre_vector[5] = '1'
        elif gen == 'Crime':
            genre_vector[6] = '1'
        elif gen == 'Documentary':
            genre_vector[7] = '1'
        elif gen == 'Drama':
            genre_vector[8] = '1'
        elif gen == 'Family':
            genre_vector[9] = '1'
        elif gen == 'Fantasy':
            genre_vector[10] = '1'
        elif gen == 'Film-Noir':
            genre_vector[11] = '1'
        elif gen == 'Game-Show':
            genre_vector[12] = '1'
        elif gen == 'History':
            genre_vector[13] = '1'
        elif gen == 'Horror':
            genre_vector[14] = '1'
        elif gen == 'Music':
            genre_vector[15] = '1'
        elif gen == 'Musical':
            genre_vector[16] = '1'
        elif gen == 'Mystery':
            genre_vector[17] = '1'
        elif gen == 'News':
            genre_vector[18] = '1'
        elif gen == 'Reality-TV':
            genre_vector[19] = '1'
        elif gen == 'Romance':
            genre_vector[20] = '1'
        elif gen == 'Sci-Fi':
            genre_vector[21] = '1'
        elif gen == 'Short':
            genre_vector[22] = '1'
        elif gen == 'Sport':
            genre_vector[23] = '1'
        elif gen == 'Talk-Show':
            genre_vector[24] = '1'
        elif gen == 'Thriller':
            genre_vector[25] = '1'
        elif gen == 'War':
            genre_vector[26] = '1'
        elif gen == 'Western':
            genre_vector[27] = '1'

    genre_vector = ''.join(genre_vector)

    link = line[2]
    if link == '':
        continue
    img_data = requests.get(link).content
    with open(str(i) + 'th' + genre_vector + '.jpg', 'wb') as handler:
        handler.write(img_data)

    if i % 100 == 0:
        print(i, "is done")

f.close()