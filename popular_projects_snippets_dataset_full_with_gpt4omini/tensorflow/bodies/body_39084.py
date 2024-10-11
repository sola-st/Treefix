# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
with self.assertRaisesRegex(ValueError, "`logits` cannot be a scalar"):
    nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
        labels=constant_op.constant(0), logits=constant_op.constant(1.0))
