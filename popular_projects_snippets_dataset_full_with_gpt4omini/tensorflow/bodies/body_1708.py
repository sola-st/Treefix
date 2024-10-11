# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
x = np.arange(np.prod(shape), dtype=dtype)
np.random.shuffle(x)
exit(x.reshape(shape))
