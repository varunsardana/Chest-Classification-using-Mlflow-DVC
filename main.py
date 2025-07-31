import os

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/varunsardana2006/Chest-Classification-using-Mlflow-DVC.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "varunsardana2006"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "6c78c96e08f9f18793ebde7944e6b4017fcfa21b"



from chestcancerClassifier import logger
from chestcancerClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chestcancerClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from chestcancerClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from chestcancerClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline








STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e




