from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textSummarizer.logging import logger


## DATA INGESTION STAGE ##
STAGE_NAME = "DATA INGESTION"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>>>> {STAGE_NAME} STAGE STARTED <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> {STAGE_NAME} STAGE COMPLETE <<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

## DATA VALIDATION STAGE ##
STAGE_NAME = "DATA VALIDATION"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>>>> {STAGE_NAME} STAGE STARTED <<<<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>>> {STAGE_NAME} STAGE COMPLETE <<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

## DATA TRANSFORMATION STAGE ##
STAGE_NAME = "DATA TRANSFORMATION"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>>>> {STAGE_NAME} STAGE STARTED <<<<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>> {STAGE_NAME} STAGE COMPLETE <<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

## MODEL TRAINING STAGE ##
STAGE_NAME = "MODEL TRAINING"

try: 
    logger.info(f"*******************")
    logger.info(f">>>>>>>> {STAGE_NAME} STAGE STARTED <<<<<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>> {STAGE_NAME} STAGE COMPLETE <<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

## MODEL EVALUATION STAGE ##
STAGE_NAME = "MODEL EVALUATION"

try: 
    logger.info(f"*******************")
    logger.info(f">>>>>>>> {STAGE_NAME} STAGE STARTED <<<<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>> {STAGE_NAME} STAGE COMPLETE <<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e