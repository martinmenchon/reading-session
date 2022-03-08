import logging
import warnings

from kedro.pipeline import Pipeline, node

from .nodes import train_test_split

warnings.filterwarnings("ignore")
_logger = logging.getLogger(__name__)


def create_pipeline():
    return Pipeline(
        [
            node(
                func=train_test_split,
                inputs=["data_cleaned", "params:steps"],
                outputs=["data_train", "y_true"],
                name="train_test_split",
            )
        ]
    )
