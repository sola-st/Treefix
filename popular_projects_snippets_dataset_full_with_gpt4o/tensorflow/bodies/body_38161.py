# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
dtypes = [
    dtypes_lib.float16,
    dtypes_lib.float32,
    dtypes_lib.float64,
    dtypes_lib.uint8,
    dtypes_lib.uint16,
    dtypes_lib.uint32,
    dtypes_lib.uint64,
    dtypes_lib.int8,
    dtypes_lib.int16,
    dtypes_lib.int32,
    dtypes_lib.int64,
]
funcs = [
    (np.less, _LT),
    (np.less_equal, _LE),
    (np.greater, _GT),
    (np.greater_equal, _GE),
]
for dtype in dtypes:
    for np_func, tf_func in funcs:
        with self.subTest(dtype=dtype, np_func=np_func, tf_func=tf_func):
            self._compareBinary(10, 5, dtype, np_func, tf_func)
logical_funcs = [(np.logical_and, _AND), (np.logical_or, _OR),
                 (np.logical_xor, _XOR), (np.equal, math_ops.equal),
                 (np.not_equal, math_ops.not_equal)]
for np_func, tf_func in logical_funcs:
    with self.subTest(np_func=np_func, tf_func=tf_func):
        self._compareBinary(True, False, dtypes_lib.bool, np_func, tf_func)
        self._compareBinary(True, True, dtypes_lib.bool, np_func, tf_func)
        self._compareBinary(False, False, dtypes_lib.bool, np_func, tf_func)
        self._compareBinary(False, True, dtypes_lib.bool, np_func, tf_func)
        self._compareBinary([True, True, False, False],
                            [True, False, True, False], dtypes_lib.bool,
                            np_func, tf_func)
self._compareUnary(True, dtypes_lib.bool, np.logical_not, _INV)
self._compareUnary(False, dtypes_lib.bool, np.logical_not, _INV)
self._compareUnary([True, False], dtypes_lib.bool, np.logical_not, _INV)
