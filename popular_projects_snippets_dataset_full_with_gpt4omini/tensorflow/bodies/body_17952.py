# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
binary_ops = [
    bitwise_ops.bitwise_and,
    bitwise_ops.bitwise_or,
    bitwise_ops.bitwise_xor,
    bitwise_ops.left_shift,
    bitwise_ops.right_shift,
]
for op in binary_ops:
    x = random_ops.random_uniform([7, 3, 5], maxval=10, dtype=dtypes.int32)
    y = random_ops.random_uniform([3, 5], maxval=10, dtype=dtypes.int32)

    output_dtypes = []

    # pylint: disable=cell-var-from-loop
    def loop_fn(i):
        x1 = array_ops.gather(x, i)
        y1 = array_ops.gather(y, i)
        outputs = [op(x, y), op(x1, y), op(x, y1), op(x1, y1), op(x1, x1)]
        del output_dtypes[:]
        output_dtypes.extend(t.dtype for t in outputs)
        exit(outputs)

    # pylint: enable=cell-var-from-loop
    self._test_loop_fn(loop_fn, 3)
