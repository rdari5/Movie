# class Movies:
#     def __init__(self, movies_file):
#         self._movies = []
#         self.read_movie_data(movies_file)

#     def read_movie_data(self, movies_file):
#         with open(movies_file, 'r') as file:
#             lines = file.read().split('\n\n')  # Phân chia dữ liệu thành các phần riêng biệt cho mỗi bộ phim
#             for line in lines:
#                 movie_info = line.split('\n')
#                 movie_name = movie_info[0]  # Tên phim là dòng đầu tiên trong mỗi phần thông tin phim
#                 movie_cast = movie_info[1].split(', ')  # Diễn viên là dòng thứ hai trong mỗi phần thông tin phim, được tách ra thành danh sách

#                 self._movies.append({
#                     'name': movie_name,
#                     'cast': movie_cast
#                 })

#     def list_movies(self):
#         for movie in self._movies:
#             print(f"Movie: {movie['name']}")
#             print("Cast: ", end="")
#             print(*movie['cast'], sep=", ")
#             print()

# if __name__ == "__main__":
#     movies = Movies('movies.txt')
#     movies.list_movies()


# class Movies:
#     def __init__(self, movies_file):
#         self._movies = []

#         with open(movies_file, encoding="utf-8") as file:
#             row_idx = 0
#             for line in file:
#                 if row_idx%3 == 0:
#                     movie_name = line.rstrip()
#                 if row_idx%3 == 1:
#                     movie_cast = line.rstrip().split(',')
#                 if row_idx%3 == 2:
#                     self._movies.append(
#                         {
#                             'name': movie_name,
#                             'cast': movie_cast
#                         }
#                     )
#                     movie_name = None
#                     movie_cast = None
#                 row_idx += 1

#         if movie_name and movie_cast:
#             # Add the last movie to the list
#             self._movies.append(
#                 {
#                     'name': movie_name,
#                     'cast': movie_cast
#                 }
#             )

# if __name__ == "__main__":
#     movies = Movies('./movies.txt')

class Movies:
    def __init__(self, movies_file):
        self._movies = []
        movie_name = None
        movie_cast = None

        with open(movies_file, encoding="utf-8") as file:
            for idx, line in enumerate(file):
                line = line.rstrip()
                if idx % 3 == 0:
                    movie_name = line
                elif idx % 3 == 1:
                    movie_cast = line.split(', ')
                elif idx % 3 == 2:
                    self._movies.append({'name': movie_name, 'cast': movie_cast})

        # Check if the last movie is complete and add it to the list
        if movie_name and movie_cast:
            self._movies.append({'name': movie_name, 'cast': movie_cast})

    def list_movies(self):
        for movie in self._movies:
            print(f"Movie: {movie['name']}")
            print("Cast: ", end="")
            print(*movie['cast'], sep=", ")
            print()

if __name__ == "__main__":
    movies = Movies('./movies.txt')
    movies.list_movies()
