import pandas as pd
from sqlalchemy import create_engine
# Postgres username, password, and database name
POSTGRES_ADDRESS = 'localhost' ## INSERT YOUR DB ADDRESS IF IT'S NOT ON PANOPLY
POSTGRES_PORT = '5432'
POSTGRES_USERNAME = 'yash' ## CHANGE THIS TO YOUR PANOPLY/POSTGRES USERNAME
POSTGRES_PASSWORD = '1234' ## CHANGE THIS TO YOUR PANOPLY/POSTGRES PASSWORD
POSTGRES_DBNAME = 'adfluencer' ## CHANGE THIS TO YOUR DATABASE NAME
# A long string that contains the necessary Postgres login information
postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'
.format(username=POSTGRES_USERNAME,
password=POSTGRES_PASSWORD,
ipaddress=POSTGRES_ADDRESS,
port=POSTGRES_PORT,
dbname=POSTGRES_DBNAME))
# Create the connection
cnx = create_engine(postgres_str)
def read_sql_tmpfile(db_engine):
    sql = "COPY users TO STDOUT WITH CSV HEADER DELIMITER ','"
    with open("/home/yash/selenium_chrome/faker_updated_6.csv", "w") as file:
        conn = db_engine.raw_connection()
        cur = conn.cursor()
        cur.copy_expert(sql, file)
        # tmpfile.seek(0)
        df = pd.read_csv('/home/yash/selenium_chrome/faker_updated_6.csv')
        # df.fillna("", inplace=True)
        return df
# sql = "COPY (SELECT * FROM a_table WHERE month=6) TO STDOUT WITH CSV DELIMITER ';'"
# with open("/mnt/results/month/table.csv", "w") as file:
#     cur.copy_expert(sql, file)

# COPY employees TO '/home/yash/selenium_chrome/faker_updated_5.csv'  WITH DELIMITER ',' CSV HEADER;
# sql_query = '''SELECT * FROM users'''

# a = read_sql_tmpfile(cnx)
# print(a)