from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///DINERS.db', echo=False)
meta = MetaData()
# resources
some_engine = create_engine('postgresql://scott:tiger@localhost/')

# create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# create a Session
session = Session()

canteen = Table(
    'CANTEEN', meta,
    Column('ID', Integer, primary_key=True),
    Column('ProviderID', Integer, primary_key=False),
    Column('Name', String),
    Column('Location', String),
    Column('time_open', Integer),
    Column('time_closed', Integer),
)

provider = Table(
        'PROVIDER', meta,
        Column('ID', Integer, primary_key=True),
        Column('ProviderName', String),
)


meta.create_all(engine)

ins = canteen.insert().values(ID=1, ProviderID=3, Name="ICT building canteen", Location="Raja 15/Mäepealse 1",
                              time_open=900, time_closed=1600)

conn = engine.connect()
result = conn.execute(ins)

conn.execute(canteen.insert(), [
    {'ID': 2, 'ProviderID': 1, 'Name': 'Economics- and social science building canteen', 'Location': 'Akadeemia tee 3',
     'time_open': 830, 'time_closed': 1830},
    {'ID': 3, 'ProviderID': 1, 'Name': "Libary canteen", 'Location': "Akadeemia tee 1/Ehitajate tee 7",
     'time_open': 830, 'time_closed': 1900},
    {'ID': 4, 'ProviderID': 2, 'Name': "Main building Deli cafe", 'Location': "Ehitajate tee 5", 'time_open': 900,
     'time_closed': 1600},
    {'ID': 5, 'ProviderID': 2, 'Name': "Main building Daily lunch restaurant", 'Location': "Ehitajate tee 5",
     'time_open': 900, 'time_closed': 1600},
    {'ID': 6, 'ProviderID': 1, 'Name': "U06 building canteen	", 'Location': "Raja 15/Mäepealse 1", 'time_open': 900,
     'time_closed': 1600},
    {'ID': 7, 'ProviderID': 2, 'Name': "Natural Science building canteen", 'Location': "Akadeemia tee 15",
     'time_open': 900, 'time_closed': 1600},
    {'ID': 8, 'ProviderID': 4, 'Name': "Sports building canteen", 'Location': "Männiliiva 7", 'time_open': 1100,
     'time_closed': 2000},
    {'ID': 9, 'ProviderID': 5, 'Name': "Sports building canteen", 'Location': "Männiliiva 7", 'time_open': 1100,
     'time_closed': 2000},
])


open_until_1800 = canteen.select().where(canteen.c.time_closed >= 1800 and canteen.c.time_open < 1615)
conn = engine.connect()
result1 = conn.execute(open_until_1800)


print()
for row in result1:
    print(row)


