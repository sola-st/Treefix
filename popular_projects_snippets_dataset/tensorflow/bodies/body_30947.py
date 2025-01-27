# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
with self.cached_session() as sess:
    x = random_ops.random_uniform([])
    fn = lambda accum, elem: accum + x * elem
    out = ctc_ops._scan(fn, constant_op.constant([0.0, 1.0, 2.0]), 23.0)
    self.assertAllClose(*sess.run([
        [23.0 + x * 0.0, 23.0 + x * 1.0, 23.0 + x * 3.0], out
    ]))
