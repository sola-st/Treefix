# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
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
