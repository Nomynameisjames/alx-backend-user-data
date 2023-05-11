#!/usr/bin/env python3
"""
    Authentication module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
        Returns a salted, hashed password, which is a byte string.
    """
    salt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return salt
