from sqlalchemy import *

def db_create():
    engine = create_engine('sqlite:///converter.db')
    engine.echo = True
    metadata = MetaData(engine)

    convert_details = Table('convert_details', metadata,
                            Column('id', Integer, primary_key=True, autoincrement=True),
                            Column('convert_attr', VARCHAR(50)),
                            Column('from_attr', VARCHAR(50)),
                            Column('to_attr', VARCHAR(50)),
                            Column('multiplication_factor', Integer)
    )

    metadata.create_all()

    value = convert_details.insert()
    value.execute(
        {'convert_attr': 'Area', 'from_attr': 'square miles', 'to_attr': 'Hectare', 'multiplication_factor': 258.99881},
        {'convert_attr': 'Currency', 'from_attr': 'USD', 'to_attr': 'INR', 'multiplication_factor': 54.35},
        {'convert_attr': 'Length', 'from_attr': 'kilometer', 'to_attr': 'meter', 'multiplication_factor': 1000},
        {'convert_attr': 'Temperature', 'from_attr': 'Celsius', 'to_attr': 'Fahrenheit',
         'multiplication_factor': 258.99881})


if __name__ == "__main__":
    print "hello"
    db_create()


