# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_xent_test.py
with self.cached_session():
    logits, targets, _ = self._Inputs()
    loss = nn_impl.sigmoid_cross_entropy_with_logits(
        labels=targets, logits=logits, name="mylogistic")
self.assertEqual("mylogistic", loss.op.name)
