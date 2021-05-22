from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Email:
    @staticmethod 
    def validate_email(email):
        results = connectToMySQL("email_val")
        is_valid= True
        if len(email["email"]) == 0:
            flash ("Input is required")
            is_valid = False
        if not EMAIL_REGEX.match(email["email"]):
            flash ("Email is not valid")
            is_valid = False
        return is_valid