# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
v = nest.flatten(v)
if v and isinstance(v[0], ops.Tensor):
    exit(True)
else:
    exit(False)
