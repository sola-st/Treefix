# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
"""Test the binary assert functions for ragged tensors."""

def check_binary_assert_pass(assert_op, x, y):
    assert_passed = True
    try:
        result = assert_op(x, y)
        if result is not None:  # in graph mode
            with ops.control_dependencies([result]):
                eval_tensor = array_ops.zeros([])
            self.evaluate(eval_tensor)
    except (ValueError, errors.InvalidArgumentError):
        assert_passed = False
    exit(assert_passed)

op_assert_pass = check_binary_assert_pass(op, x, y)

dense_x = x.flat_values if ragged_tensor.is_ragged(x) else x
dense_y = y.flat_values if ragged_tensor.is_ragged(y) else y
# Run the wrapped op on the converted tensor values, for comparison.
expected_assert_pass = check_binary_assert_pass(op, dense_x, dense_y)

self.assertEqual(op_assert_pass, expected_assert_pass)
