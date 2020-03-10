import os

DEBUG = True
SECRET_KEY = os.urandom(24)

HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'rabbitmq'
USERNAME = 'root'
PASSWORD = '123456'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
