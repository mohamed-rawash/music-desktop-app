import json
from pathlib import Path



DB_FILE_PATH = r"D:\python projects\Qt\music_app\music_db.json"
db_music = json.load(open(DB_FILE_PATH, "r"))

class SongLoader:
    @staticmethod
    def get_singers(user_id: str) -> list:
        if user_id not in db_music:
            db_music[user_id] = []
        names = []
        for singer_info in db_music[user_id]:
            names.append(
                (
                    singer_info.get("name"),
                    singer_info.get("image_path")
                )
            )
        return names

    @staticmethod
    def get_songs_list(user_id: str, singer_index: int):
        song_paths = db_music[user_id][singer_index]["songs"]
        singer_name = db_music[user_id][singer_index]["name"]
        singer_image_path = db_music[user_id][singer_index]["image_path"]
        songs = []
        for song_path in song_paths:
            file_name = Path(song_path).name.split(".")[0]
            songs.append(
                (
                    file_name,
                    song_path,
                )
            )
        return singer_name, singer_image_path, songs

    @staticmethod
    def get_singer_image(user_id: str, singer_index: int) -> str:
        pass

    @staticmethod
    def add_new_singer(user_id: str, singer_name: str, singer_image_path: str, songs_list: list) -> None:
        if user_id not in db_music:
            db_music[user_id] = []
        new_entery = {
            "name": singer_name,
            "image_path": singer_image_path,
            "songs": songs_list
        }
        db_music[user_id].append(new_entery)
        json.dump(db_music, open(DB_FILE_PATH, "w"), indent=4)
