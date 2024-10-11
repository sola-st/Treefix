# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
tensor = constant_op.constant(1, name="my_tensor")
desired_rank = 1
with self.assertRaisesRegex(ValueError, "fail.*must have rank 1"):
    with ops.control_dependencies(
        [check_ops.assert_rank(
            tensor, desired_rank, message="fail")]):
        self.evaluate(array_ops.identity(tensor))
