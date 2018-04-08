

# Create Parent Class for movies and other video types
class Video():
    #initialize Video Class
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


#Pass Video as argument to inherit class Video attributes
class Movie(Video):
    
    def __init__(self, title, duration, movie_storyline, poster_image, trailer_youtube):
        #initialize Parent class for inheritance
        Video.__init__(self, title, duration)
        #assign class Movie attributes
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube



    
        
