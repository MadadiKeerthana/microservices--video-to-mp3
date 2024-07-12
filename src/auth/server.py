
#json web tokens for auth
import jwt

#datatime to set expiry for auth
import datetime

#os for env vars for sql connections
import os

#using flask to create server
from flask import Flask, request

#allows to import from mysql
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

#config
#has all configurations variables needed
server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST") 
# print(server.config["MYSQL_HOST"]) #'export MYSQL_HOST=localhost' to test
server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST") 
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")

@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401
    
    # check df for username and password
    cur = mysql.connection.cursor()
    res = cur.execute(
        "SELECT email, password FROM user WHERE email=%s", (auth.username)
    )
    
    if res > 0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[1]
        
        if auth.username != email or auth.password != password:
            return "invalid credentials", 401
        else:
            # return createJWT(auth.username, os.environ.get("JWT_SECRET"), True)
            return "working on it", 200
    else: 
        return "invalid credentials", 401



