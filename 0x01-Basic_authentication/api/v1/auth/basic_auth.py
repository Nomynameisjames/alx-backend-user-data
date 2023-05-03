#!/usr/bin/env python3
"""
    import files
"""
import base64
from .auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        """
            Returns Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
