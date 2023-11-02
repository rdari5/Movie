from movies import Movies

movies = Movies('./movies.txt')


def movie_names(name):

def list_movies():


def author_names(name):
    name = str(name).lower()
    for i in range(len(movies._movies)):
        castFound = False
        for j in range(len(movies._movies[i]['cast'])):
            if movies._movies[i]['cast'][j].lower().__contains__(name):
                castFound = True
                
        
        if castFound:
            print(movies._movies[i]['name'])
            print("[", end = ' ')
            for k in range(0,len(movies._movies[i]['cast'])):
                if movies._movies[i]['cast'][k].lower().__contains__(name):
                    print(movies._movies[i]['cast'][k], end = ' ')
            
            print("]")

option = ' '


while option != 'q':
    print("q: quit") 
    print("sn: search movie names")
    print("sc: search casts")
    print("list: print all the movie names")
    option = input("").lower()

    if option == "sn":
        word = input("enter a word to search: ")
        movie_names(word)

    elif option == "sc":
        word = input("enter a word to search: ")
        author_names(word)
    
    elif option == "list":
       list_movies()


