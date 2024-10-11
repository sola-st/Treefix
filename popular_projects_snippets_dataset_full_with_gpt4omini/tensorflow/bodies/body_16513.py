# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_xent_test.py
with self.cached_session():
    logits, targets, pos_weight, _ = self._Inputs()
    loss = nn_impl.weighted_cross_entropy_with_logits(
        targets=targets, logits=logits, pos_weight=pos_weight, name="mybce")
self.assertEqual("mybce", loss.op.name)
