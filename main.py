from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig,training_pipeline_config,DataValidationConfig
from networksecurity.components.Data_validation import DataValidation
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
        dataingestionartifcats=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion completed successfully")
        print(data_ingestion_config,dataingestionartifcats )

        data_validation_config=DataValidationConfig(training_pipeline_config)
        data_validation=DataValidation(dataingestionartifcats,data_validation_config) 
        data_validation_artifacts=data_validation.Initiate_data_Validation()
        logging.info("Data Validation completed successfully")
        print(data_validation_artifacts)
    except Exception as e:
           raise NetworkSecurityException(e,sys)