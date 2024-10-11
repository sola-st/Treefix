# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ragged_batch_test.py
exit((ops.convert_to_tensor(x),
        math_ops.range(x),
        array_ops.fill([x, 2], x)))
