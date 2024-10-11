# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_ops_test.py
with self.session() as sess:
    with self.test_scope():
        a = array_ops.placeholder(np.float32)
        index = array_ops.placeholder(np.int32)
        out = math_ops.reduce_sum(a, index)
    with self.assertRaisesWithPredicateMatch(
        errors_impl.InvalidArgumentError,
        'Axes contains duplicate dimension'):
        sess.run(out, {a: [10, 20, 30], index: [0, 0]})
