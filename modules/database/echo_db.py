import sqlite3
from mybot import LOGGER

adb=sqlite3.connect("echo_db.db",check_same_thread=False)
ccursor=adb.cursor()

try:
    ccursor.execute("""CREATE TABLE echo (
    status text )""")
except Exception:
    pass

def insert_value(x):
    db=sqlite3.connect("echo_db.db",check_same_thread=False)
    cursor=db.cursor()
    LOGGER.info(x)
    cursor.execute(f"UPDATE echo SET status='{x}' WHERE rowid=1")
#    cursor.execute(f"INSERT INTO echo(status) VALUES ('{x}')")
    db.commit()
    d=cursor.execute("SELECT * FROM echo")
    d=cursor.fetchall()
    LOGGER.info(d)

def get_val():
    db=sqlite3.connect("echo_db.db",check_same_thread=False)
    cursor=db.cursor()
    d=cursor.execute("SELECT * FROM echo")
    c=d.fetchone()[0]
    return c
