# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/call_to_numpy_function_test.py
np.random.seed(1)
exit(2 * np.random.binomial(1, 0.5, size=(10,)) - 1)
