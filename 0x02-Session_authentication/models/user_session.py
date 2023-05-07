#!/usr/bin/env python3
"""
    import files
"""
from models.base import Base


class UserSession(Base):
    """
        UserSession class inherits from Base
    """
    def __init__(self, *args: list, **kwargs: dict):
        """
            init method
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get("user_id", "")
        self.session_id = kwargs.get("session_id", "")
