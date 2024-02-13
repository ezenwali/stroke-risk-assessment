from dataclasses import dataclass
import os
import sys
import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from src.common.custom_logger import CustomLogger
from src.common.exceptions import CustomException


@dataclass
class DataIngestionConfig:
    """Configuration"""

    dir_name = "artifacts"
    train_data_path: str = os.path.join(dir_name, "train.csv")
    test_data_path: str = os.path.join(dir_name, "test.csv")


class DataIngestion:
    """Import data from any source ie. locally, or from database"""

    def __init__(self, test_size=0.2):
        self.config = DataIngestionConfig()
        self.logger = CustomLogger()
        self.test_size = test_size
        os.makedirs(self.config.dir_name, exist_ok=True)

    def initiate_data_ingestion_from_csv(self):
        """Import raw data from CSV from the data folder"""
        try:
            self.logger.log_info("Commenced reading raw data from the data folder")
            df = pd.read_csv("../../data/raw.csv")
            train_set, test_set = self._split_raw_data(df)

        except FileNotFoundError as e:
            exc_tb = e.__traceback__
            custom_exception = CustomException(
                "The required file 'raw.csv' was not found. Please ensure the file path is available.",
                exc_tb,
            )
            self.logger.log_error(custom_exception)
            raise custom_exception from e
        except Exception as e:
            exc_tb = e.__traceback__
            custom_exception = CustomException("Unable to ingest data", exc_tb)
            self.logger.log_error(custom_exception)
            raise custom_exception from e

    def _split_raw_data(self, df: DataFrame) -> tuple[DataFrame, DataFrame]:
        """Private method to split raw data into train and test sets"""
        train_set, test_set = train_test_split(
            df, test_size=self.test_size, random_state=42
        )
        train_set.to_csv(self.config.train_data_path, index=False, header=True)
        test_set.to_csv(self.config.test_data_path, index=False, header=True)

        self.logger.log_info("Saved training set and test set to artifact folder")

        return train_set, test_set


dd = DataIngestion()
dd.initiate_data_ingestion_from_csv()
