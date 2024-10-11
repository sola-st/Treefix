# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
# logits, targets: float arrays of the same shape.
assert logits.shape == targets.shape
pred = 1. / (1. + np.exp(-logits))
eps = 0.0001
pred = np.minimum(np.maximum(pred, eps), 1 - eps)
exit(-targets * np.log(pred) - (1. - targets) * np.log(1. - pred))
