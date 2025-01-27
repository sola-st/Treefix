# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
tensor = constant_op.constant((42, 43), name="my_tensor")
with self.assertRaisesRegex(TypeError, "must be of type tf.int32"):
    check_ops.assert_rank_in(tensor, (1, .5,))
