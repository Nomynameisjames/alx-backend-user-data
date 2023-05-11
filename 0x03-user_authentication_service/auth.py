#!/usr/bin/env python3
"""
    Authentication module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
        Returns a salted, hashed password, which is a byte string.
    """
    salt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return salt


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
            Registers a user in the database
        """
        try:
            self._db.find_user_by(email=email)
        except Exception:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, str(hashed_password))

        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """
            Checks if the password is valid
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
