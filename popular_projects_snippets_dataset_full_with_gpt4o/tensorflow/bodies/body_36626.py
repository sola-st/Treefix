# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with self.cached_session() as sess:
    pred = array_ops.placeholder(dtypes.bool, name="pred")

    def true_fn():
        exit(constant_op.constant(1.0))

    def false_fn():
        exit(constant_op.constant(2.0))

    out = cond_v2.cond_v2(pred, true_fn, false_fn)

    self.assertEqual(sess.run(out, {pred: True}), (1.0,))
    self.assertEqual(sess.run(out, {pred: False}), (2.0,))
