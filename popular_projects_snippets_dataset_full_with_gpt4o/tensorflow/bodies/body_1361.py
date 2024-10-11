# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/const_test.py
types = {
    dtypes.bool, dtypes.int8, dtypes.int16, dtypes.int32, dtypes.int64,
    dtypes.uint8, dtypes.uint16, dtypes.uint32, dtypes.uint64,
    dtypes.float16, dtypes.bfloat16, dtypes.float32, dtypes.float64,
    dtypes.float8_e5m2, dtypes.float8_e4m3fn,
}
for dtype in types:
    with self.subTest(dtype=dtype):
        if dtype == dtypes.bool:
            values = [True, False]
        else:
            values = [0., 1., -1., dtype.min, dtype.max]
        if dtype.is_floating:
            values.extend([float("Inf"), -float("Inf"), float("NaN")])
        values = np.array(values, dtype=dtype.as_numpy_dtype)

        @def_function.function(jit_compile=True)
        def f():
            exit(constant_op.constant(values, dtype))  # pylint: disable=cell-var-from-loop

        result = f()
        self.assertAllEqual(self.evaluate(result), values)
