#!/usr/bin/env python3
"""
    Authentication module
"""
import bcrypt
from db import DB
from user import User
from uuid import uuid4


def _generate_uuid() -> str:
    """
        Returns a string representation of a new UUID
    """
    return str(uuid4())


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
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """
            Creates a session ID for the user
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """
            Returns the user associated with the session ID
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user.email
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
            Destroys the session ID
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """
            Generates a reset password token
        """
        try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token
        except Exception:
            raise ValueError
