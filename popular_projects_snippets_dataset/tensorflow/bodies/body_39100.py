# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
with ops_lib.Graph().as_default(), self.session(use_gpu=False) as sess:
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                expected_regex):
        labels = array_ops.placeholder(dtypes.int32, shape=[None, 1])
        logits = array_ops.placeholder(dtypes.float32, shape=[None, 3])
        ce = nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
            labels=array_ops.squeeze(labels), logits=logits)
        labels_v2 = np.zeros((1, 1), dtype=np.int32)
        logits_v2 = np.random.randn(1, 3)
        sess.run([ce], feed_dict={labels: labels_v2, logits: logits_v2})
