from app import app
from models import db, Playlist, Song, PlaylistSong

db.drop_all()
db.create_all()

s1 = Song(
  title="Go Baby",
  artist="Sumana"
)

s2 = Song(
  title="High Sky",
  artist="John Doe"
)

s3 = Song(
  title="Kill Joy",
  artist="Anjana"
)

p1 = Playlist(
  name="Rock And Roll",
  description="A fun theme song"
)

p2 = Playlist(
  name="Country Music",
  description="Relaxing Music"
)

db.session.add_all([s1, s2, s3])
db.session.add_all([p1, p2])
db.session.commit()

ps1 = PlaylistSong(
  song_id = 1,
  playlist_id = 2
)

ps2 = PlaylistSong(
  song_id = 2,
  playlist_id = 1
)

ps3 = PlaylistSong(
  song_id = 3,
  playlist_id = 1
)

db.session.add_all([ps1, ps2, ps3])
db.session.commit()

