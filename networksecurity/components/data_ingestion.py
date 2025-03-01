from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


##configuration file for the data ingestion config

from networksecurity.entity.config_entity import DataIngestionConfig,training_pipeline_config
from networksecurity.constants import training_pipeline 
import os
import sys
import pandas as pd
import numpy as np

import pymongo 
from typing import List
from sklearn.model_selection import train_test_split 

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")  

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config

        except Exception as e:  
            raise NetworkSecurityException(e,sys)   
        

    def export_collection_as_dataframe(self):

        '''
        __summery__ : This method will export the collection from the mongo db as a dataframe
        Raises:
        NetworkSecurityException: [description]
        Returns:
        [type]: [description]
        


        '''



        try:
            database_name=self.data_ingestion_config.database_name  
            collection_name=self.data_ingestion_config.collection_name
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
           # self.database=self.mongo_client[database_name]
            collection=self.mongo_client[database_name][collection_name]
            df=pd.DataFrame(list(collection.find()))

            if "_id" in df.columns:
                df.drop(columns=["_id"],inplace=True,axis=1)
                

            df.replace({"na":np.nan},inplace=True)    
            #    pas
            #    dataframe=
        except Exception as e:
            raise NetworkSecurityException(e,sys)
            


             



        def initiate_data_ingestion(self):
            try:
                pass
            #    pas
            #    dataframe=
            except Exception as e:
                raise NetworkSecurityException(e,sys)
            


             