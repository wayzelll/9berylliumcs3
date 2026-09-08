def opm():

  def __init__(username, genre, artist, date, listeners):
    username.attribute1 = genre
    username.attribute2 = artist
    username.__private_attribute = date
    username.__private_attribute = listeners

  def searchGenre(genre):
    genre_ = str(input("Type your OPM genre: "))
    print(f"{genre_} is now playing")

  def searchArtist(artist):
    artist_ = str(input("Type the artist you like: "))
    print(f"{artist_}'s songs are now playing")

  def createPlaylist():
    playlist_ = genre_, artist_
    playlist_ = str(input("Enter your playlist's name"))
    print(playlist_)
  
opm(__init__, searchGenre, searchArtist, createPlaylist)
    
    
  
    
    
  
  
                  
