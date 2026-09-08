class OPM:

    def __init__(self, genre, artist, date, listeners):
        self.genre = genre
        self.artist = artist
        self._date = date
        self._listeners = listeners
        self.playlists = []  # Added initialization for playlists list

    def search_genre(self):
        genre_ = input("Type your OPM genre: ")
        print(f"{genre_} is now playing")
        return genre_

    def search_artist(self):
        artist_ = input("Type the artist you like: ")
        print(f"{artist_}'s songs are now playing")
        return artist_

    def create_playlist(self, genre, artist):
        playlist_name = input("Enter your playlist's name: ")
        full_title = f"{playlist_name} ({genre} - {artist} songs)"
        self.playlists.append(full_title)  # Appends created playlist to the list
        print(f"Playlist '{full_title}' created!")

    def delete_playlist(self):
        if not self.playlists:
            print("No playlists available to delete.")
            return

        print("\nYour Playlists:")
        # Fixed reference from self.playlists to match self context
        for idx, playlist in enumerate(self.playlists, 1):
            print(f"{idx}. {playlist}")

        name_to_delete = input(
            "\nEnter the name or number of the playlist to delete: "
        )

        # Check if user entered a number index
        if name_to_delete.isdigit():
            index = int(name_to_delete) - 1
            if 0 <= index < len(self.playlists):
                removed = self.playlists.pop(index)
                print(f"Deleted playlist: '{removed}'")
                return

        # Check if user entered the exact playlist title/string
        for playlist in self.playlists:
            if name_to_delete.lower() in playlist.lower():
                self.playlists.remove(playlist)
                print(f"Deleted playlist: '{playlist}'")
                return

        print("Playlist not found.")


# Example execution
user = OPM("Alternative Rock", "Eraserheads", "1990s", 10000000)
selected_genre = user.search_genre()
selected_artist = user.search_artist()
user.create_playlist(selected_genre, selected_artist)
print("Music now, enjoy forever")

user.delete_playlist()
  
  
                  
