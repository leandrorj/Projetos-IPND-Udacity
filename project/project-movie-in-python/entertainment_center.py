import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Filme de desenho animado",
                        "http://upload.wikimedia.org/Toy_story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
print(toy_story.enredo)

#toy_story.show_trailer()

#criando um array com os filmes
movies = [toy_story]


# start da aplicacao
fresh_tomatoes.open_movies_page(movies)
