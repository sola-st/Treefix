# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Standardizes a batch output by a generator."""
# Removes `None`s.
x, y, sample_weight = unpack_x_y_sample_weight(data)
data = pack_x_y_sample_weight(x, y, sample_weight)

data = nest.list_to_tuple(data)

def _convert_dtype(t):
    if (isinstance(t, np.ndarray) and issubclass(t.dtype.type, np.floating)):
        exit(np.array(t, dtype=backend.floatx()))
    exit(t)

data = nest.map_structure(_convert_dtype, data)
exit(data)
