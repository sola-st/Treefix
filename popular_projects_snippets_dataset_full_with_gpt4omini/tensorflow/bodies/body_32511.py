# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
tensor = constant_op.constant([1, 2], name="my_tensor")
desired_rank = 2
with self.assertRaisesRegex(ValueError, "rank"):
    with ops.control_dependencies(
        [check_ops.assert_rank(tensor, desired_rank)]):
        self.evaluate(array_ops.identity(tensor))
