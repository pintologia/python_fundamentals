current_movies={
    'The Grinch': '11:00am',
    'Rudolph': '1:00am',
    'frosty the snowman': '2:00pm'
}

print('We are showing the following movies: \n')
for key in current_movies:
    print(key)
    
movie= input('what movie would you like the show time for? \n')
showtime = current_movies.get(movie)

if showtime == None:
    print('Requested movie isnt playing')
else:
    print(movie, 'is playing at', showtime)
