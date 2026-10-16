def add_song(songs):
    title = input("enter the song's title:").strip()
    artist = input("enter the artist:").strip()
    minutes = int(input("enter duration (minutes):"))
    seconds = int(input("enter duration (seconds):"))
    duration = minutes * 60 + seconds
    new_song = {"title": title, "artist": artist, "duration": duration, "plays": 0}
    songs.append(new_song)



def record_listen(songs):
    title = input("enter the song's title:").strip()
    for song in songs:
        if song["title"] == title:
            song["plays"] += 1
            print(f" listened to {title}")
            return
    print(f"Song '{title}' not found.") 

def generate_wrapped(songs):
    if len(songs) == 0:
        print("No songs in the list.")
        return
    total_songs = len(songs)
    total_plays = 0
    for song in songs:
        total_plays += song["plays"]
    total_seconds = 0
    for song in songs:
        total_seconds = total_seconds + song["duration"] * song["plays"]
    total_minutes = int(total_seconds / 60)
    print("========== YOUR SPOTIFY WRAPPED ==========")
    print()
    print(f"Total Songs: {total_songs}")
    print(f"Total Plays: {total_plays}")
    print(f"Total Listening Time: {total_minutes} minutes")
    print()
    if total_plays == 0:
        print("No songs have been played yet.")
    else:
        most_played = songs[0]
        for song in songs:
            if song["plays"] > most_played["plays"]:
                most_played = song
        print("Your Most Played Song:")
        print(f"{most_played['title']} - {most_played['artist']} ({most_played['plays']} plays)")
    print()
    print("==========================================")