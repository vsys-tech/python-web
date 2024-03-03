from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from pymongo.cursor import Cursor


class MongoDB:
    __url = "mongodb://192.168.1.152:27017/"
    __db_config = "?authSource=admin&retryWrites=true&w=majority"

    __client: MongoClient = None
    __db_name: str = ''
    __db: Database = None

    def __init__(self):
        pass

    def properties(self, db_name: str):
        self.__db_name = db_name
        return self

    def connect(self) -> Database:
        self.__client = MongoClient(self.__url + self.__db_name + self.__db_config)
        self.__db = self.__client[self.__db_name]
        return self.__db

    def close(self) -> None:
        self.__client.close()


if __name__ == '__main__':

    client: MongoClient = None
    playerCollection: Collection = None
    cursor: Cursor = None
    db: Database = None

    mongodb = MongoDB()
    mongodb.properties("cricket")
    db = mongodb.connect()
    playerCollection = db['player']

    cursor = playerCollection.find()

    for player in cursor:
        print(player)

    cursor.close()
    mongodb.close()
