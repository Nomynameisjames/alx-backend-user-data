#!/usr/bin/env python3
"""
    import files
"""
import os
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """
        SessionExpAuth class that inherits from SessionAuth
        add session expiration feature to SessionAuth
    """
    def __init__(self):
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
            create session method that create a Session ID for a user_id
            by calling super() - super() will call the create_session()
            method of SessionAuth
        """
        if user_id is None:
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
            user id for session id method that returns a User ID based on
            a Session ID
        """
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id:
            return None
        if "created_at" not in self.user_id_by_session_id[session_id]:
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id]["user_id"]
        created_at = self.user_id_by_session_id[session_id]["created_at"]
        expired_time = created_at + timedelta(seconds=self.session_duration)
        if expired_time < datetime.now():
            return None
        return self.user_id_by_session_id[session_id]["user_id"]
