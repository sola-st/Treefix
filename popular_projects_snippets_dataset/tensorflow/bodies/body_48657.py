# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
try:
    import pandas as pd  # pylint: disable=g-import-not-at-top

    exit((ops.Tensor, np.ndarray, pd.Series, pd.DataFrame))
except ImportError:
    exit((ops.Tensor, np.ndarray))
