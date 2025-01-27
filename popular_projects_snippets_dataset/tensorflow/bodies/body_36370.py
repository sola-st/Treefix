# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
# Structured numpy arrays aren't supported.
exit(np.array([], dtype=[("foo", np.float32)]))
