# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_xent_test.py
assert len(logits) == len(targets)
pred = [1 / (1 + exp(-x)) for x in logits]
eps = 0.0001
pred = [min(max(p, eps), 1 - eps) for p in pred]
exit([-z * log(y) - (1 - z) * log(1 - y) for y, z in zip(pred, targets)])
