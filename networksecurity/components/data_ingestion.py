from networksecurity.entity.artifcat_entity import DataIngestionArtifact
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
        NetworkSecurityException: __description__
        Returns:
        __type__: __description__
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
            return df
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def export_data_into_the_feature_store(self,dataframe:pd.DataFrame):
        '''
        __summary__: This method will export the data into the feature store
        Args:

        dataframe(pd.DataFrame): The dataframe which needs to be exported
        Raises:
        NetworkSecurityException: __description__
        Returns:
        __type__: __description__
        '''
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            #creating the folder
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)

            dataframe.to_csv(self.data_ingestion_config.feature_store_file_path,index=False)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        try:
            train_set,test_set=train_test_split(dataframe,
                                                test_size=self.data_ingestion_config.train_test_split_ratio
                                                ) 
            logging.info("perfrmed Train test split on the Dataset")

            logging.info("Splitng Process Completed and exited the process ")

            dir_path=os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dir_path,exist_ok=True)

            logging.info("Exporting the Train and test files into the location")

            train_set.to_csv(self.data_ingestion_config.train_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.test_file_path,index=False,header=True)
            logging.info("Exported the Train and test files into the location")

        except Exception as e:
            raise NetworkSecurityException(e,sys)
            
    
    
    def initiate_data_ingestion(self):
        try:
            dataframe=self.export_collection_as_dataframe()
            dataframe=self.export_data_into_the_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            DataIngestionArtificats=DataIngestionArtifact(train_file_path=self.data_ingestion_config.train_file_path,
                                                          test_file_path=self.data_ingestion_config.test_file_path
                                                          )
            #self.split_data(dataframe)
            #    pas
            #    dataf rame=
            return DataIngestionArtificats
        except Exception as e:
            raise NetworkSecurityException(e,sys)
