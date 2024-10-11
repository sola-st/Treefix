# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
peek = next(x)
exit((peek, itertools.chain([peek], x)))
