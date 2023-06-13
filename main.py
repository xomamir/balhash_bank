#Local
from database.core import Connection

import datetime

#Python
from decouple import config 

from database.models.users import User
from database.models.accounts import Accounts
from database.models.cards import Card


my_connection: Connection = Connection(
    host=config('DB_HOST', str),
    port=config('DB_PORT', int),
    user=config('DB_USER', str),
    password=config('DB_PASSWORD', str),
    dbname=config('DB_NAME', str)
)


if __name__ == '__main__':
    my_connection.create_tables()
    # User.create(
    #     conn=my_connection.conn,
    #     id=1,
    #     first_name='rezvan',
    #     last_name='shar',
    #     date_of_birth=datetime.datetime(
    #     year=2005,
    #     month=5,
    #     day=15),
    #     iin='050515123234',
    #     phone_number= '7799410034'
    # )
    # Accounts.create(
    #     conn=my_connection.conn,
    #     number='bob',
    #     owner_id='friday',
    #     date_of_birth=datetime.datetime(
    #     year=1998,
    #     month=5,
    #     day=15),
    #     iin='980515123234',
    #     phone_number= '7789410034'
    # )
    # Card.create(
    #     conn=my_connection.conn,
    #     first_name='bob',
    #     last_name='friday',
    #     date_of_birth=datetime.datetime(
    #     year=1998,
    #     month=5,
    #     day=15),
    #     iin='980515123234',
    #     phone_number= '7789410034'
    # )
    User.get_all(conn=my_connection.conn)
    User.get(conn=my_connection.conn, first_name= 'bob')