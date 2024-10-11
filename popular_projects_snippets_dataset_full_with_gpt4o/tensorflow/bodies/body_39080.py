# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
labels = [4, 3, 0, -1]
logits = [[1., 1., 1., 1.], [1., 1., 1., 1.], [1., 2., 3., 4.],
          [1., 2., 3., 4.]]
with self.assertRaisesRegex(
    (errors_impl.InvalidArgumentError, errors_impl.UnknownError),
    expected_regex):
    self.evaluate(
        nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
            labels=labels, logits=logits))
