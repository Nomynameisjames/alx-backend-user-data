#!/usr/bin/env python3
"""
    Encrypts a password using bcrypt
"""
import bcrypt
from bcrypt import hashpw

"""
    Implement a hash_password function that expects one string argument name
    password and returns a salted, hashed password, which is a byte string.

    objective:
        Use the bcrypt package to perform the hashing (with hashpw).
"""


def hash_password(password: str) -> bytes:
    """ Encrypts a password using bcrypt """
    return hashpw(password.encode('utf-8'), bcrypt.gensalt())
