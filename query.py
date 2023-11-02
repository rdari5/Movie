from movies import Movies  # Assuming movies.py contains the Movies class

def movie_names(movies, name):
    for movie in movies._movies:
        if name.lower() in movie['name'].lower():
            print(movie['name'])

def list_movies(movies):
    for movie in movies._movies:
        print(movie['name'])

def author_names(movies, name):
    name = name.lower()
    for movie in movies._movies:
        if any(name in cast.lower() for cast in movie['cast']):
            print(movie['name'])
            print("[", end=' ')
            print(*[cast for cast in movie['cast'] if name in cast.lower()], end=' ')
            print("]")

def main():
    movies_instance = Movies('./movies.txt')  # Initialize the Movies class

    option = ' '

    while option != 'q':
        print("q: quit")
        print("sn: search movie names")
        print("sc: search casts")
        print("list: print all the movie names")
        option = input("Enter an option: ").lower()

        if option == "sn":
            word = input("Enter a word to search movie names: ")
            movie_names(movies_instance, word)
        elif option == "sc":
            word = input("Enter a word to search casts: ")
            author_names(movies_instance, word)
        elif option == "list":
            list_movies(movies_instance)

if __name__ == "__main__":
    main()

