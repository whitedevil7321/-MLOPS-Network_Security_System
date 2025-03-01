from datetime import datetime
import os
from networksecurity.constants import training_pipeline
from networksecurity.entity import config_entity 


print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFCATS_DIR)



class training_pipeline_config:
    def __init__(self,timestamp=datetime.now().strftime('%m_%d_%Y_%H_%M_%S')):
        self.timestamp=timestamp
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifacts_name=training_pipeline.ARTIFCATS_DIR
        self.artifacts_dir=os.path.join(self.artifacts_name,timestamp)
        self.timestamp:str = timestamp
                # self.file_name=training_pipeline.FILE_NAME
        # self.target_column=training_pipeline.TARGET_COLUMN
        # self.train_file_name=training_pipeline.TRAIN_FILE_NAME
        # self.test_file_name=training_pipeline.TEST_FILE_NAME




class DataIngestionConfig:
    def __init__(self,training_pipeline_config:training_pipeline_config):
        self.data_ingestion_dir=os.path.join(training_pipeline_config.artifacts_dir,training_pipeline.DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,training_pipeline.FILE_NAME )
        self.train_file_path=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_NAME)
        self.test_file_path=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TEST_FILE_NAME)
        self.data_ingestion_collection_name:str=training_pipeline.DATA_INGESTION_COLLECTTION_NAME
        self.data_ingestion_database_name:str=training_pipeline.DATA_INGESTION_DATABASE_NAME
        self.train_test_split_ratio:float=training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name=training_pipeline.DATA_INGESTION_COLLECTTION_NAME
        self.database_name=training_pipeline.DATA_INGESTION_DATABASE_NAME



