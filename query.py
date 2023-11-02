from movies import Movies

movies = Movies('./movies.txt')


def movie_names(name):

def list_movies():

def author_names(name):

option = ' '


while option != 'q':
    print("q: quit") 
    print("sn: search movie names")
    print("sc: search casts")
    print("list: print all the movie names")
    option = scan("").lower()

    if option == "sn":
        word = scan("enter a word to search: ")
     #   movie_names(word)

    elif option == "sc":
        word = scan("enter a word to search: ")
      #  author_names(word)
    
    elif option == "list":
       # list_movies()

