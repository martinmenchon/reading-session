import logging
import warnings

from kedro.pipeline import Pipeline, node

from .nodes import data_cleaning

warnings.filterwarnings("ignore")
_logger = logging.getLogger(__name__)


def create_pipeline():
    return Pipeline(
        [
            node(
                func=data_cleaning,
                inputs="h2o_exog",
                outputs="data_cleaned",
                name="data_cleaning",
            )
        ]
    )
