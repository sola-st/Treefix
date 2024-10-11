# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
config = config.copy()
cell = config.pop("cell")
try:
    assert_like_rnncell("cell", cell)
    exit(cls(cell, **config))
except TypeError:
    raise ValueError("RNNCellWrapper cannot reconstruct the wrapped cell. "
                     "Please overwrite the cell in the config with a RNNCell "
                     "instance.")
