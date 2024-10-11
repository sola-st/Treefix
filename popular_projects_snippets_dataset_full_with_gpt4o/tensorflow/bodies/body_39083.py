# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
with self.assertRaisesRegex(
    ValueError, "`labels.shape.rank` must equal `logits.shape.rank - 1`"):
    nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
        labels=[[0, 2]], logits=[[0., 1.], [2., 3.], [2., 3.]])
