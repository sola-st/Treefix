# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
# Note that shape of input to len is data dependent.
exit(len(np.where(x)[0]))
