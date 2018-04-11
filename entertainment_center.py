import media
import fresh_tomatoes

# create a series of Movie instances
toy_story = media.Movie(
    "Toy Story",
    "1hr 21min",
    "Some story line",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",  # noqa
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "2hr 42min",
    "Some other planet movie",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

boondock_saints = media.Movie(
    "Boondock Saints",
    "1hr 48min",
    "Brother who avenge in the name of God",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/The_Boondock_Saints_poster.jpeg/220px-The_Boondock_Saints_poster.jpeg",  # noqa
    "https://www.youtube.com/watch?v=ydXojYfCF3I")

chisum = media.Movie(
    "Chisum",
    "1hr 51min",
    "Man who avenges and protects",
    "https://upload.wikimedia.org/wikipedia/en/thumb/d/d7/Chisum1.jpg/220px-Chisum1.jpg",  # noqa
    "https://www.youtube.com/watch?v=1p9r03roFaw")

man_on_fire = media.Movie(
    "Man on Fire",
    "1hr 53min",
    "Bodyguard risks all to save little girl",
    "https://upload.wikimedia.org/wikipedia/en/thumb/e/e8/Man_on_fireposter.jpg/220px-Man_on_fireposter.jpg",  # noqa
    "https://www.youtube.com/watch?v=eDDh50B6kA4")

kleine_arschloch = media.Movie(
    "Das Kleine Arschloch",
    "1hr 22min",
    "Story of a troublesome young man",
    "https://ia.media-imdb.com/images/M/MV5BMTI1MjkxMjUwMl5BMl5BanBnXkFtZTcwNzAxNjkyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=jhYbV_7ryPo")

# create an array of Movie instances to provide as an
# argument for fresh_tomatoes.open_movies()
movies = [toy_story, avatar, boondock_saints, chisum,
          man_on_fire, kleine_arschloch]

fresh_tomatoes.open_movies_page(movies)
