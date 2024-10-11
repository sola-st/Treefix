# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
with ops_lib.Graph().as_default(), self.session():
    labels = array_ops.placeholder(np.int32)
    y = nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
        labels=labels, logits=[[7.]])
    with self.assertRaisesOpError(expected_error_message):
        y.eval(feed_dict={labels: 0})
