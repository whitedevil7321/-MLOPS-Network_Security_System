from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig,training_pipeline_config
from networksecurity.constants import training_pipeline
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import os
import sys
import pandas as pd
import numpy as np




if __name__=='__main__':
    try:
        training_pipeline_config=training_pipeline_config()    
        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)

        logging.info("Ingesting the data into the feature store")
        data_ingestion_artifcats=data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifcats )
    except Exception as e:
           raise NetworkSecurityException(e,sys)