# Python implementation of the music player application using object-oriented programming (OOP) concepts

class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.rating = 0

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def set_rating(self, rating):
        self.rating = rating

    def get_rating(self):
        return self.rating


class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audios = []
        self.rating = 0

    def add_audio(self, audio):
        self.audios.append(audio)

    def search_audio_by_name(self, name):
        for audio in self.audios:
            if audio.get_name() == name:
                return audio
        return None

    def calculate_average_rating(self):
        total_ratings = sum([audio.get_rating() for audio in self.audios])
        self.rating = total_ratings / len(self.audios) if len(self.audios) > 0 else 0
        return self.rating

    def get_rating(self):
        return self.rating


class MusicPlayer:
    def __init__(self):
        self.playlists = []

    def create_playlist(self, name, genre):
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist

    def search_playlist_by_name(self, name):
        for playlist in self.playlists:
            if playlist.name == name:
                return playlist
        return None


# Example Usage:

# Creating audio objects
audio1 = Audio("Song 1", "https://example.com/song1.mp3")
audio2 = Audio("Song 2", "https://example.com/song2.mp3")
audio3 = Audio("Song 3", "https://example.com/song3.mp3")

# Creating playlist objects
playlist1 = Playlist("Playlist 1", "Pop")
playlist2 = Playlist("Playlist 2", "Rock")

# Adding audios to playlists
playlist1.add_audio(audio1)
playlist1.add_audio(audio2)
playlist2.add_audio(audio3)

# Creating music player
music_player = MusicPlayer()

# Adding playlists to music player
music_player.playlists.append(playlist1)
music_player.playlists.append(playlist2)

# Searching for playlist by name
found_playlist = music_player.search_playlist_by_name("Playlist 1")
if found_playlist:
    print("Playlist found:", found_playlist.name)
else:
    print("Playlist not found")

# Calculating average rating for playlist
playlist1.add_audio(audio1)
audio1.set_rating(4)
audio2.set_rating(5)
playlist1.calculate_average_rating()
print("Average rating for Playlist 1:", playlist1.get_rating())