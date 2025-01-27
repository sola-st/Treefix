# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
i = next(iterator)
v.assign_add(math_ops.reduce_mean(i))
