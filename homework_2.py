# -*- coding: utf-8 -*-
"""
complete script to add a record in customers table
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///DINERS.db', echo=False)

Base = declarative_base()


class Provider(Base):
    """
    Create table Provider
    """

    __tablename__ = 'PROVIDER'

    id = Column(Integer, primary_key=True)
    providerName = Column(String)


class Canteen(Base):
    """
    Create table Canteen
    """

    __tablename__ = 'CANTEEN'
    id = Column(Integer, primary_key=True)
    providerID = Column(Integer, ForeignKey('PROVIDER.id'))
    name = Column(String)
    location = Column(String)
    time_open = Column(Integer)
    time_closed = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def create_tables_data():
    """
    Create data for tables
    :return:
    """

    try:
        session.add_all([
            Provider(id=1, providerName="Rahva Toit"),
            Provider(id=2, providerName="Baltic Restaurants ESTONIA AS"),
            Provider(id=3, providerName="TTÜ Sport OÜ"),
            Provider(id=4, providerName="Bitstop Kohvik OÜ"),
        ])

        c1 = Canteen(id=1, providerID=3, name="ICT building canteen", location="Raja 15/Mäepealse 1", time_open=900,
                     time_closed=1600)

        session.add(c1)

        session.add_all([
            Canteen(id=2, providerID=1, name="Economics- and social science building canteen",
                    location="Akadeemia tee 3",
                    time_open=830, time_closed=1830),
            Canteen(id=3, providerID=1, name="Libary canteen", location="Akadeemia tee 1/Ehitajate tee 7",
                    time_open=830,
                    time_closed=1900),
            Canteen(id=4, providerID=2, name="Main building Deli cafe", location="Ehitajate tee 5", time_open=900,
                    time_closed=1600),
            Canteen(id=5, providerID=2, name="Main building Daily lunch restaurant", location="Ehitajate tee 5",
                    time_open=900,
                    time_closed=1600),
            Canteen(id=6, providerID=1, name="U06 building canteen", location="Raja 15/Mäepealse 1", time_open=900,
                    time_closed=1600),
            Canteen(id=7, providerID=2, name="Natural Science building canteen", location="Akadeemia tee 15",
                    time_open=900,
                    time_closed=1600),
            Canteen(id=8, providerID=3, name="Sports building canteen", location="Männiliiva 7", time_open=1100,
                    time_closed=2000),
            Canteen(id=9, providerID=4, name="bitstop KOHVIK", location="Lossi 20", time_open=1100,
                    time_closed=1600),
        ])
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def open_canteens():
    """
    Function that prints which canteens are open between 16.15-18.00
    :return:
    """
    try:
        result = session.query(Canteen).filter(Canteen.time_open <= 1615, Canteen.time_closed >= 1800)
        print("Canteens that are open 16.15-18.00")
        for row in result:
            print("Canteen name: ", row.name)
    except:
        session.rollback()
        raise
    finally:
        session.close()


def serviced_by_rahva_toit():
    """
    Function that prints which canteens are serviced by Rahva Toit
    :return:
    """
    try:
        result = session.query(Canteen).join(Provider, Provider.id == Canteen.providerID).filter(
            Provider.providerName == "Rahva Toit")
        print("Canteens serviced by Rahva Toit:")
        for row in result:
            print("Canteen name: ", row.name)
    except:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    create_tables_data()
    open_canteens()
    serviced_by_rahva_toit()
