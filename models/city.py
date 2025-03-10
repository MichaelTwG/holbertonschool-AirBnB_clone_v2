#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),
                      ForeignKey("states.id", ondelete="CASCADE"),
                      nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        from sqlalchemy.orm import relationship

        places = relationship("Place", backref="cities", cascade="all, delete")

    else:
        places = []
