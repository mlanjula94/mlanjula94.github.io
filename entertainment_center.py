import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of boy and his toys that comes alow",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

deadpool = media.Movie("Deadpool",
                       "Story of a sarcastic villan",
                       "http://t2.gstatic.com/images?q=tbn:ANd9GcTvrIHJfasS6poy34esN1O5hZonXaiqfEZb4WbnbAa9qJCIL8_9",
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk")

#print(avatar.storyline)
#deadpool.show_trailer()

movies = [toy_story, avatar, deadpool]
index.open_movies_page(movies)
#print(media.Movie.__module__)
