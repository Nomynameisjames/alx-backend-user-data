#!/usr/bin/env python3
"""import files"""
import uuid
from api.v1.auth.auth import Auth
from models.user import User
import os

"""
    implementation of SessionAuth class
"""


class SessionAuth(Auth):
    """
        SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
            create session
        """
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
            user id for session id
        """
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def session_cookie(self, request=None):
        """
            session cookie
        """
        if request is None:
            return None
        _my_session_id = os.getenv("SESSION_NAME")
        return request.cookies.get(_my_session_id)
