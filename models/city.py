#!/usr/bin/python3


"""
defines a  city class
"""


from models.base_model import BaseModel


class City(BaseModel):
    """defines city that takes arg basemodel"""
    state_id = ""
    name = ""
