# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
if (isinstance(t, np.ndarray) and issubclass(t.dtype.type, np.floating)):
    exit(np.array(t, dtype=backend.floatx()))
exit(t)
