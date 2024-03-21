import pandas as pd 
import snowflake.connector
import os

def import_snowflake():
    snowflake_account = os.environ.get('SNOWFLAKE_ACCOUNT')
    snowflake_password = os.environ.get('SNOWFLAKE_PASSWORD')

    connection = snowflake.connector.connect(
        user='omiddehkordi',
        password=snowflake_password,
        account=snowflake_account,
        warehouse='compute_wh',
        database='ballers_reference',
        schema='public'
    )


    query = "SELECT * FROM nba_rookies"
    cursor = connection.cursor()
    cursor.execute(query)

    data = cursor.fetchall()
    nba_rookies = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])

    cursor.close()
    connection.close()

    return nba_rookies
