#!/usr/bin/python3


"""
Class User
"""


from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes for class, takes in Arg Basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
