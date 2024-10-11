# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
tensor_rank0 = constant_op.constant(42, name="my_tensor")
for desired_ranks in ((0, 1, 2), (1, 0, 2), (1, 2, 0)):
    with ops.control_dependencies([
        check_ops.assert_rank_in(tensor_rank0, desired_ranks)]):
        self.evaluate(array_ops.identity(tensor_rank0))
