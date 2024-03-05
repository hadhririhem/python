from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# model the class after the friend table from our database
class User :
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('email_schema').query_db(query)
        # Create an empty list to append our instances of friends
        emails = []
        # Iterate over the db results and create instances of friends with cls.
        for email in results:
            emails.append( cls(email) )
        return emails
    @classmethod
    def save(cls, data) :
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL('email_schema').query_db(query, data)
    @staticmethod
    def valid_email(user):
        is_valid= True
        query = "SELECT * from emails WHERE email = %(email)s"
        results = connectToMySQL('email_schema').query_db(query, user)
        if len(results) >= 1 :
            flash("email already taken, try again")
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]) : 
            flash("The email you entered is not valid please try again")
            is_valid = False
        return is_valid
            