# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
exit(nest.map_structure(lambda d: array_ops.gather(d, i, axis=0), data))
