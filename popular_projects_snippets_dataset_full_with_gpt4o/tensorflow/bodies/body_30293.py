# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
for dtype in _TEST_DTYPES:
    if not dtype.is_integer:
        self._testGradientsSimple(dtype)
        self._testGradientsSimpleVariable(dtype)
