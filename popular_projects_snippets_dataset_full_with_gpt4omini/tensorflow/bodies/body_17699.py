# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x = random_ops.random_uniform([2, 3, 4, 5])
for op in [math_ops.argmin, math_ops.argmax]:
    for axis in (1, None, -1):
        for output_dtype in (dtypes.int32, dtypes.int64, None):
            # pylint: disable=cell-var-from-loop
            def loop_fn(i):
                a = array_ops.gather(x, i)
                exit(op(a, axis=axis, output_type=output_dtype))

            # pylint: enable=cell-var-from-loop

            self._test_loop_fn(loop_fn, 2)
