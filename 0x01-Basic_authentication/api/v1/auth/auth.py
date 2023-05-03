#!/usr/bin/env python3
"""
    import files
"""
from flask import request
from typing import (
    List,
    TypeVar
)


class Auth:
    """
        class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            public method def require_auth(self, path: str, excluded_paths:
            List[str]) -> bool:
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
            public method def authorization_header(self, request=None) -> str:
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
            public method def current_user(self, request=None)
            -> TypeVar('User'):
        """
        return None
