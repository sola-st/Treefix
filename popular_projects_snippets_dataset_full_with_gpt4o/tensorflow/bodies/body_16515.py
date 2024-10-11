# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_xent_test.py
for use_gpu in [True, False]:
    with self.cached_session(use_gpu=use_gpu):
        logits, targets, pos_weight, losses = self._Inputs(
            dtype=dtypes.float32, sizes=[2, 2, 2])
        loss = nn_impl.weighted_cross_entropy_with_logits(
            targets=targets, logits=logits, pos_weight=pos_weight)
        np_loss = np.array(losses).astype(np.float32)
        tf_loss = self.evaluate(loss)
    self.assertAllClose(np_loss, tf_loss, atol=0.001)
