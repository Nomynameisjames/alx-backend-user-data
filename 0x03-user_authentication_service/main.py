#!/usr/bin/env python3
"""
Main file
"""
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from auth import _hash_password

my_db = DB()

def print_obj():
    print(User.__tablename__)

    for column in User.__table__.columns:
        print("{}: {}".format(column, column.type))

    print("\n")


def run_add_user():
    user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
    print(user_1.id)

    user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
    print(user_2.id)

def run_find_user_by():
    user = my_db.add_user("test@test.com", "PwdHashed")
    print(user.id)

    find_user = my_db.find_user_by(email="test@test.com")
    print(find_user.id)

    try:
        find_user = my_db.find_user_by(email="test2@test.com")
        print(find_user.id)
    except NoResultFound:
        print("Not found")

    try:
        find_user = my_db.find_user_by(no_email="test@test.com")
        print(find_user.id)
    except InvalidRequestError:
        print("Invalid")

def run_update_user():
    email = 'test@test.com'
    hashed_password = "hashedPwd"

    user = my_db.add_user(email, hashed_password)
    print(user.id)

    try:
        my_db.update_user(user.id, hashed_password='NewPwd')
        print("Password updated")
    except ValueError:
        print("Error")

def run_validate_hashed_password():
    print(_hash_password("Hello Holberton"))

if __name__ == "__main__":
    #print_obj()
    #run_add_user()
    #run_find_user_by()
    #run_update_user()
    run_validate_hashed_password()

