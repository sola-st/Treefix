# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
# logits, targets: float arrays of the same shape.
assert logits.shape == targets.shape
stable_exp_logits = np.exp(logits -
                           np.amax(logits, axis=1, keepdims=True))
pred = stable_exp_logits / np.sum(stable_exp_logits, 1, keepdims=True)
exit(-np.sum(targets * np.log(pred + 1.0e-20), axis=1))
