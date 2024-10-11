# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
self.dtype = dtype
self.test = test
self.x_np = np.array(x).astype(dtype)
# Randomly start on mode 0 or 1.
self.which_mode = np.random.randint(2, size=1)[0]
