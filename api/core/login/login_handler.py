import secrets
import bcrypt
import os

from datetime import datetime, timedelta
from dotenv import load_dotenv

from api.core.mongo import MongoLogin, MongoUser

load_dotenv()


class LoginHandler:
    __PEPPER_SECRET = os.getenv("PEPPER_SECRET")

    @classmethod
    def hash_password(cls, password: str) -> str:
        """Hash a password using bcrypt with salt and pepper."""
        password = password.encode()
        peppered_password = password + cls.__PEPPER_SECRET.encode()  # Add pepper from .env
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(peppered_password, salt)
        return hashed.decode()

    @classmethod
    def verify_password(cls, password: str, hashed_password: str) -> bool:
        """Verify the password against the stored hash."""
        peppered_password = password.encode() + cls.__PEPPER_SECRET.encode()
        return bcrypt.checkpw(peppered_password, hashed_password.encode())

    def __init__(self):
        self.mongo_login = MongoLogin()
        self.mongo_user = MongoUser()

    def authenticate(self, username, password):
        if username is not None and password is not None:
            user = self.mongo_user.get_user_by_username(username)
            if self.verify_password(password, user.get("password")):
                token = secrets.token_urlsafe(32)
                self.mongo_login.add_token(
                    user_id=user.get("id"),
                    token=token,
                    expiration=datetime.now() + timedelta(days=1)
                )
                return token

    def authenticate_with_token(self, token):
        return (
            token is None or
            self.mongo_login.is_token_valid(token, datetime.now())
        )
