#!/usr/bin/python3
"""
Defines class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Representation of a user


    Attributes:
        email(str): user email
        password(str): user password
        first_name(str): first name
        last_name(str): last name

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
