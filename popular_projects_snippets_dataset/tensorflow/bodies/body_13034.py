# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
assert len(x.shape) == 2
m = x.max(1)[:, np.newaxis]
u = x - m
exit(u - np.log(np.sum(np.exp(u), 1, keepdims=True)))
