# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
tensor = constant_op.constant([1, 2], name="my_tensor")
desired_rank = 0
with ops.control_dependencies(
    [check_ops.assert_rank_at_least(tensor, desired_rank)]):
    self.evaluate(array_ops.identity(tensor))
