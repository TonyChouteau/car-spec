from . import DB


class MongoLogin:
    def __init__(self):
        self.mongo_token = DB["token"]

    def add_token(self, user_id, token, expiration):
        self.mongo_token.delete_many({
            "user_id": user_id
        })
        self.mongo_token.insert_one({
            "token": token,
            "user_id": user_id,
            "expiration": expiration
        })

    def is_token_valid(self, token, now):
        return self.mongo_token.find_one({
            "token": token,
            "expiration": {
                "$gt": now
            }
        }) is not None


