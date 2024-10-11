# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
# Test case for GitHub issue 53300.
# Error message is `Shapes of all inputs must match` in eager mode,
# and `Shapes ...` in graph mode. Below is to capture both:
with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                            r"Shapes"):
    with self.session():
        t = [array_ops.zeros([0, 3]), array_ops.zeros([1, 3])]
        self.evaluate(array_ops.stack(t))
