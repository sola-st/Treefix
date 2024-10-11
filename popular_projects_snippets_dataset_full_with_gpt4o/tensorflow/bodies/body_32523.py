# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
tensor_rank1 = constant_op.constant((42, 43), name="my_tensor")
with self.assertRaisesRegex(ValueError, "rank"):
    with ops.control_dependencies([
        check_ops.assert_rank_in(tensor_rank1, (0, 2))]):
        self.evaluate(array_ops.identity(tensor_rank1))
