# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
tensor_rank0 = constant_op.constant(42, name="my_tensor")
with self.assertRaisesRegex(ValueError, "fail.*must have rank.*in.*1.*2"):
    with ops.control_dependencies([
        check_ops.assert_rank_in(tensor_rank0, (1, 2), message="fail")]):
        self.evaluate(array_ops.identity(tensor_rank0))
