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


"""
    Implement an is_valid function that expects 2 arguments and returns a
    boolean.

    Arguments:
        hashed_password: bytes type
        password: string type
"""


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ ensures the provided password matches the hashed password """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
