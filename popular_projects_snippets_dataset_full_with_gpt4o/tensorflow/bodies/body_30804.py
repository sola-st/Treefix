# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softsign_op_test.py
np_softsign = self._npSoftsign(np_features)
with self.cached_session(use_gpu=use_gpu):
    softsign = nn_ops.softsign(np_features)
    tf_softsign = self.evaluate(softsign)
self.assertAllClose(np_softsign, tf_softsign)
self.assertShapeEqual(np_softsign, softsign)
