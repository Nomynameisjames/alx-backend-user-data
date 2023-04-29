#!/usr/bin/env python3
"""import files"""
from typing import List
import re
import logging
import os
import mysql.connector

"""
     function called filter_datum that returns the log message obfuscated:
    Arguments:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is separating all
        fields in the log line (message)
        function should use a regex to replace occurrences of certain field
        values.
        filter_datum should be less than 5 lines long and use re.sub to
        perform the substitution with a single regex.
"""
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
        function called filter_datum that returns the log message obfuscated
    """
    for item in fields:
        message = re.sub(item+'=.*?'+separator,
                         item+'='+redaction+separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """
        Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
            redact the message of LogRecord instance
        """
        message = super(RedactingFormatter, self).format(record)
        redact = filter_datum(self.fields, self.REDACTION,
                              message, self.SEPARATOR)
        return redact


def get_logger() -> logging.Logger:
    """
        function that takes no arguments and returns a logging.Logger
        object.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
        function that returns a connector to the database
    """
    User = os.getenv('PERSONAL_DATA_DB_USERNAME') or "root"
    Password = os.getenv('PERSONAL_DATA_DB_PASSWORD') or ""
    Host = os.getenv('PERSONAL_DATA_DB_HOST') or "localhost"
    DB_name = os.getenv('PERSONAL_DATA_DB_NAME')
    Connection = mysql.connector.connect(user=User,
                                         password=Password,
                                         host=Host,
                                         database=DB_name)
    return Connection


def main():
    """
        main function
    """
    database = get_db()
    logger = get_logger()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = cursor.column_names
    for row in cursor:
        message = "".join("{}={}; ".format(k, v) for k, v in zip(fields, row))
        logger.info(message.strip())
    cursor.close()
    database.close()


if __name__ == "__main__":
    main()
