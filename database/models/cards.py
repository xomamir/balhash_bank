import datetime

from database.core import Connection

from database.models.accounts import Accounts

class Card:
    """Object from db. Card."""

    id: int
    number: str
    account: Accounts
    cvv: str
    data_end: datetime.datetime
    is_active: bool
    pin: str

    @staticmethod
    def create(
        conn: Connection,
        number:str,
        account: Accounts,
        cvv: str,
        data_end: datetime,
        is_active:bool,
        pin:str
    ):
        with conn.cursor() as cur:
            cur.execute(
                f"""
                INSERT INTO card(
                    number,
                    account_id,
                    cvv,
                    data_end,
                    is_active,
                    pin
                )
                VALUES(

                    '{number}',
                    '{account_id}',
                    '{cvv}',
                    '{data_end}',
                    '{is_active}',
                    '{pin}'
                )"""
            )