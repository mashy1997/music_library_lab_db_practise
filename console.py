from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository 

# album_repository.delete_all()
# artist_repository.delete_all()

artist1 = Artist("Beyonce")
artist_repository.save(artist1)
artist2 = Artist("Lana Del Rey")
artist_repository.save(artist2)
artist3 = Artist("Nicki Minaj")
artist_repository.save(artist3)

album1 = Album("Lemonade", "Hip Hop", artist1)
album_repository.save(album1)
album2 = Album("Lust for Life", "Indie", artist2)
album_repository.save(album2)
album3 = Album("Queen", "Rap", artist3)
album_repository.save(album3)


artist_repository.select_all()

