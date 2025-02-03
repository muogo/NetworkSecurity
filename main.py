from NetworkSecurity.components.data_ingestion import DataIngestion
from NetworkSecurity.components.data_validation import DataValidation
from NetworkSecurity.components.data_transformation import DataTransformation
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from NetworkSecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("data initiation Completed")
        print(dataingestionartifact)
        
        
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)
        
        
        data_trasformation_config=DataTransformationConfig(trainingpipelineconfig)
        logging.info("data Transformation started")
        data_trasformation=DataTransformation(data_validation_artifact,data_trasformation_config)
        data_trasformation_artiface=data_trasformation.initiate_data_transformation()
        print(data_trasformation_artiface)
        logging.info("data Transformation completed")
        
        
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)