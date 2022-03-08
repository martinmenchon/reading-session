import logging
import warnings

from kedro.pipeline import Pipeline, node

from .nodes import results

warnings.filterwarnings("ignore")
_logger = logging.getLogger(__name__)


def create_pipeline():
    return Pipeline(
        [
            node(
                func=results,
                inputs=["data_train", "y_true", "y_pred"],
                outputs=None,
                name="results",
            )
        ]
    )
