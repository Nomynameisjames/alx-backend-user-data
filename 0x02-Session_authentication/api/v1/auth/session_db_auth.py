#!/usr/bin/env python3
"""
    import files
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """
        SessionDBAuth class - inherits from SessionExpAuth
    """
    def create_session(self, user_id=None):
        """
            create_session - create a session and stores new instance of
            UserSession and returns the Session ID
        """
        if user_id is None:
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
            user_id_for_session_id - return user_id from session_id by
            requesting UserSession in the database based on session_id
        """
        if session_id is None:
            return None
        try:
            user_session = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if len(user_session) == 0:
            return None
        if user_session[0].session_id != session_id:
            return None
        if self.session_duration <= 0:
            return user_session[0].user_id
        if user_session[0].created_at is None:
            return None
        if (user_session[0].created_at +
                timedelta(seconds=self.session_duration) < datetime.now()):
            return None
        return user_session[0].user_id

    def destroy_session(self, request=None):
        """
            destroy_session - destroy a UserSession based on the Session ID
            from the request cookie
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        try:
            user_session = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if len(user_session) == 0:
            return False
        if user_session[0].session_id != session_id:
            return False
        user_session[0].remove()
        return True
