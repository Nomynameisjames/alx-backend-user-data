#!/usr/bin/env python3
"""import files"""
import uuid
from api.v1.auth.auth import Auth
from models.user import User

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
