import pymongo
import config

def getDatabase():
    conn = pymongo.MongoClient(config.database_url, config.database_port)
    return conn.daytour