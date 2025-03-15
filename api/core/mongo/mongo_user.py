from . import DB


class MongoUser:
    def __init__(self):
        self.mongo_user = DB["user"]

    def get_user_by_username(self, login):
        return self.mongo_user.find_one({
            "username": login,
        })

    def get_user_by_id(self, user_id):
        return self.mongo_user.find_one({
            "user_id": user_id
        })
