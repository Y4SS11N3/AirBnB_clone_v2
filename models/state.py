#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """
        Returns the list of City instances with
        state_id equal to the current State.id
        """
        city_list = models.storage.all(City)
        return [city for city in city_list if city.state_id == self.id]
