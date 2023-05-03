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

    def decode_base64_authorization_header(
             self, base64_auth_header: str) -> str:
        """
            Returns decoded value of a Base64 string
        """
        if base64_auth_header is None:
            return None
        if not isinstance(base64_auth_header, str):
            return None
        try:
            decode = base64.b64decode(base64_auth_header.encode('utf-8')
                                      ).decode('utf-8')
            return decode
        except Exception:
            return None
