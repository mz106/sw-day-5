movie_titles = ['rocky', 'starwars', 'batman']

print('Add a new movie title')
new_movie = input('  >  ')

print(new_movie)

if new_movie not in movie_titles:
    movie_titles.append(new_movie)
else:
    print(f'The movie {new_movie} is already on the list')

print(movie_titles)