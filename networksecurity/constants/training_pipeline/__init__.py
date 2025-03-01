import os
import sys
import numpy as np
import pandas as pd

'''
Defining the constants variables for the training pipeline
'''

TARGET_COLUMN="Result"
PIPELINE_NAME:str="Network_Security"
ARTIFCATS_DIR:str="Artifacts"
FILE_NAME:str="Networkdata.csv"


TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"





'''
Data ingestion related constatants starts with data ingestion var name
'''

DATA_INGESTION_COLLECTTION_NAME: str = 'Network_Data'
DATA_INGESTION_DATABASE_NAME:str ="Network_Security"
DATA_INGESTION_DIR_NAME: str="Data_Ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="Feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float=0.2

