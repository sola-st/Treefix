# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_xent_test.py
for use_gpu in [True, False]:
    for dtype in [dtypes.float32, dtypes.float16]:
        with self.cached_session(use_gpu=use_gpu):
            logits, targets, losses = self._Inputs(dtype=dtype, sizes=[2, 2, 2])
            loss = nn_impl.sigmoid_cross_entropy_with_logits(
                labels=targets, logits=logits)
            np_loss = np.array(losses).astype(np.float32)
            tf_loss = self.evaluate(loss)
        self.assertAllClose(np_loss, tf_loss, atol=0.001)
