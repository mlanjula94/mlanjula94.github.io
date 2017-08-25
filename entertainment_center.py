import media
import index
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

hangover = media.Movie("Hangover",
                       "A bachelor party gone wrong",
                       "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
                       "https://www.youtube.com/watch?v=tcdUhdOlz9M")

spiderman = media.Movie("Spider-Man",
                        "A teen with a spider like power becomes a super hero",
                        "http://cafmp.com/wp-content/uploads/2016/05/Spider-Man.jpg",
                        "https://www.youtube.com/watch?v=oNE0zRNyXuc")

saving_private_rayan = media.Movie("Saving Private Rayan",
                                   "The mission is a man",
                                   "https://i.pinimg.com/736x/06/cb/33/06cb338efcf3ac37a90caad05fd356a2--saving-private-ryan-matt-damon.jpg",
                                   "https://www.youtube.com/watch?v=zwhP5b4tD6g")

#print(avatar.storyline)
#deadpool.show_trailer()

movies = [toy_story, avatar, deadpool, hangover, spiderman, saving_private_rayan]
index.open_movies_page(movies)
#print(media.Movie.__module__)
