import logging
import warnings

from kedro.pipeline import Pipeline, node

from .nodes import run_forecasting

warnings.filterwarnings("ignore")
_logger = logging.getLogger(__name__)


def create_pipeline():
    return Pipeline(
        [
            node(
                func=run_forecasting,
                inputs=["data_train", "params:steps", "params:lags"],
                outputs="y_pred",
                name="forecasting",
            )
        ]
    )
