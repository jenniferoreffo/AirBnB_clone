#!/usr/bin/python3


"""
Defines review class
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class takes in arg Basemodel """
    place_id = ""
    user_id = ""
    text = ""
