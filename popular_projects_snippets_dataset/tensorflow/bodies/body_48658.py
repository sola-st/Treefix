# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
try:
    from scipy.sparse import issparse  # pylint: disable=g-import-not-at-top

    exit(issparse(x))
except ImportError:
    exit(False)
