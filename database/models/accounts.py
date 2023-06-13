import datetime

from database.core import Connection

class Accounts:
    
    ''' Object from db. Accounts.'''
    id: int
    number: str
    owner_id: int
    balance: float
    types: str

    @staticmethod 
    def create(
    id: int,
    conn: Connection,
    number: str,
    owner_id: int,
    balance: float,
    types: str
    ):
        with conn.cursor() as cur:
            cur.execute(f'''
                INSERT INTO accounts(
                    number,
                    owner_id,
                    balance,
                    type)
                VALUES(
                    '{number}',
                    '{owner_id}',
                    '{balance}',
                    '{types}')
                '''
            )