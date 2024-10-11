# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
assert x.shape
total_elements = np.prod(x.shape)
nonzeros = np.count_nonzero(x.flatten())
exit(1.0 - nonzeros / total_elements)
