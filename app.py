import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Julia Chen in 3308'

@app.route('/db_test')
def db_test():
    #conn = psycopg2.connect("postgresql://juch5453_postgresql_user:tD7NdcQPZM3jriCWxcklHUPaaID93k9I@dpg-cqij026ehbks73buv140-a.oregon-postgres.render.com/juch5453_postgresql")
    conn = psycopg2.connect("postgresql://juch5453_postgresql_user:tD7NdcQPZM3jriCWxcklHUPaaID93k9I@dpg-cqij026ehbks73buv140-a/juch5453_postgresql")
    conn.close()
    return "Database Connection Successful"
