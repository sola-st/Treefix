# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
dtypes = [
    dtypes_lib.float16,
    dtypes_lib.float32,
    dtypes_lib.float64,
    dtypes_lib.bfloat16,
    dtypes_lib.uint8,
    dtypes_lib.uint16,
    dtypes_lib.uint32,
    dtypes_lib.uint64,
    dtypes_lib.int8,
    dtypes_lib.int16,
    dtypes_lib.int32,
    dtypes_lib.int64,
    dtypes_lib.complex64,
    dtypes_lib.complex128,
]
funcs = [
    (np.add, _ADD),
    (np.subtract, _SUB),
    (np.multiply, _MUL),
    (np.power, _POW),
    (np.true_divide, _TRUEDIV),
    (np.floor_divide, _FLOORDIV),
    (np.mod, _MOD),
]
for dtype in dtypes:
    for np_func, tf_func in funcs:
        with self.subTest(dtype=dtype, np_func=np_func, tf_func=tf_func):
            if dtype in (dtypes_lib.complex64,
                         dtypes_lib.complex128) and tf_func in (_FLOORDIV, _MOD):
                continue  # floordiv makes no sense for complex
            if dtype in (dtypes_lib.uint8, dtypes_lib.uint16, dtypes_lib.uint32,
                         dtypes_lib.uint64) and tf_func == _POW:
                continue  # power not supported for unsigned types
            self._compareBinary(10, 3, dtype, np_func, tf_func)
