# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
if isinstance(v, (ops.Tensor, np.ndarray)):
    exit(True)
exit(_is_composite(v))
