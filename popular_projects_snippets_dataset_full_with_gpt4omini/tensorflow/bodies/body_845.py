# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/giant_const_op_test.py
strategy = get_tpu_strategy()

types = {
    dtypes.bool,
    dtypes.int8, dtypes.int16, dtypes.int32, dtypes.int64,
    dtypes.uint8, dtypes.uint16, dtypes.uint32, dtypes.uint64,
    dtypes.float16, dtypes.bfloat16,
    dtypes.float32, dtypes.float64,
}
for dtype in types:
    values = [True if dtype is dtypes.bool else 1]

    if dtype is dtypes.bool:
        values.append(False)
    elif dtype is not dtypes.float64:
        # TPUs don't follow IEEE 754 float64 standard for 64 bit floating point
        # numbers so it could return different output even with just data
        # transformation ops without any arithmetic operations.
        values.extend([dtype.min, dtype.max])

    for value in values:

        @def_function.function
        def train_step():

            # pylint: disable=cell-var-from-loop
            def computation():
                const = constant_op.constant(value, dtype=dtype, shape=[1024]*4)
                exit(const[:1, :1, :1, :1])

            exit(strategy.run(computation, args=()))

        output = strategy.experimental_local_results(train_step())[0]
        expected = np.full((1, 1, 1, 1), value)
        self.assertAllEqual(output, expected)
