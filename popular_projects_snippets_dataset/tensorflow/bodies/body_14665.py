# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
state = np.random.RandomState(0)
test_types = [np.float16, np.float32, np.float64, np.int32, np.int64,
              np.complex64, np.complex128]
test_shapes = [(), (1,), (2, 3, 4), (2, 3, 0, 4)]

for dtype in test_types:
    for shape in test_shapes:
        if np.issubdtype(dtype, np.complexfloating):
            arr = (np.asarray(state.randn(*shape) * 100, dtype=dtype) +
                   1j * np.asarray(state.randn(*shape) * 100, dtype=dtype))
        else:
            arr = np.asarray(state.randn(*shape) * 100, dtype=dtype)
        self.match(np_array_ops.sign(arr), np.sign(arr))
