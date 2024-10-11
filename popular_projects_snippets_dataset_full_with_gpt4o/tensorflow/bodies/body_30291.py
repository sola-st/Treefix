# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
for dtype in _TEST_DTYPES:
    for _ in range(5):
        self._RunAndVerify(dtype)
        self._RunAndVerify(dtype, large_num_splits=True)
        self._RunAndVerifyVariable(dtype)
        self._RunAndVerifyVariable(dtype, large_num_splits=True)
