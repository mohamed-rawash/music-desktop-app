import json


DB_PATH = r"D:\python projects\Qt\music_app\users.json"
users_db = json.load(open(DB_PATH, "r"))

class User:
    def __init__(self, user_name: str, password: str):
        self.__user_name = user_name
        self.__password = password
        self.__user_id = 0

    def login(self):
        is_existed = False
        for user in users_db["users"]:
            if user["name"] == self.__user_name and user["password"] == self.__password:
                is_existed = True
                self.__user_id = user["id"]
                break
        return is_existed

    def register(self):
        user_id = int(users_db["index_counter"])
        users_db["index_counter"] = user_id
        user_info = {"name": self.__user_name, "password": self.__password, "id": user_id}
        users_db['users'].append(user_info)
        json.dump(users_db, open(DB_PATH, "w"), indent=4)
        return True

    def get_user_id(self):
        return self.__user_id