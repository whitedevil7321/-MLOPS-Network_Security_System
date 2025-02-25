import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
#MONGO_DB_NAME=os.getenv("MONGO_DB_NAME")
#MONGO_DB_COLLECTION=os.getenv("MONGO_DB_COLLECTION")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
          
    def csv_to_json_converter(self,filepath):
        try:
            logger.logging.info("Enter the csv_to_json_converter method")
            #read the csv file
            data=pd.read_csv(filepath)
            data.reset_index(drop=True,inplace=True)
             
            #convert the data into json
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_to_mongo(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

if __name__=='__main__':
    try:
        FILE_PATH=os.path.join(r"C:\Users\Admin\Desktop\Network_Security_system\Network_Data\phisingData.csv")
        DATABASE="Network_Security"
        COLLECTION="Network_Data"
        networkobj=NetworkDataExtract()
        records=networkobj.csv_to_json_converter(FILE_PATH)
        no_of_records=networkobj.insert_data_to_mongo(records,DATABASE,COLLECTION)
        print(f"Number of records inserted into the collection {no_of_records}")
        #print(networkobj.insert_data_to_mongo(networkobj.csv_to_json_converter(FILE_PATH),DATABASE,COLLECTION)) 
        #logger.logging.info("Enter the main block")
        #network_data=NetworkDataExtract()
        #records=network_data.csv_to_json_converter("data.csv")
        #print(network_data.insert_data_to_mongo(records,"Network_Security","Network_Data"))
    except Exception as e:
        raise NetworkSecurityException(e,sys)        

        