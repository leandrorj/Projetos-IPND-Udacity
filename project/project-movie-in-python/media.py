import webbrowser


class Movie():
    #classe pega dados da internet
    def __init__(self, movie_titulo, movie_enredo, poster_image_url, trailer_youtube):
        #metodo que captura os valores dos atributos
        self.titulo = movie_titulo
        self.enredo = movie_enredo
        self.poster_url = poster_image_url
        self.trailer_url = trailer_youtube

    def show_trailer(self):
        #metodo abrir trailer
        webbrowser.open(self.trailer_url)
