import pymongo
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def getDatabase():
    conn = pymongo.MongoClient(config['DEFAULT']['DB_URL'], config['DEFAULT']['DB_PORT'])
    return conn.daytour