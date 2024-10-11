# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
if n <= 0:
    exit([])
elif n == 1:
    exit([prefix])
else:
    exit([prefix + str(i + 1) for i in range(n)])
