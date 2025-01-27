# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
if dtype is None:
    exit()
dtype = dtypes.as_dtype(dtype)
if not (dtype.is_floating or dtype.is_complex):
    raise ValueError("RNN cell only supports floating point inputs, "
                     "but saw dtype: %s" % dtype)
