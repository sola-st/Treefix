# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_xent_test.py
sizes = [4, 2]
with self.cached_session():
    logits, targets, pos_weight, _ = self._Inputs(sizes=sizes)
    loss = nn_impl.weighted_cross_entropy_with_logits(
        targets=targets, logits=logits, pos_weight=pos_weight)
    err = gradient_checker.compute_gradient_error(logits, sizes, loss, sizes)
print("logistic loss gradient err = ", err)
self.assertLess(err, 1e-7)
