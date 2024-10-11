# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_xent_test.py
sizes = [4, 2]
with self.cached_session():
    logits, targets, _ = self._Inputs(sizes=sizes)
    loss = nn_impl.sigmoid_cross_entropy_with_logits(
        labels=targets, logits=logits)
    err = gradient_checker.compute_gradient_error(logits, sizes, loss, sizes)
print("logistic loss gradient err = ", err)
self.assertLess(err, 1e-7)
