# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_xent_test.py
x = [-100, -2, -2, 0, 2, 2, 2, 100] if x is None else x
y = [0, 0, 1, 0, 0, 1, 0.5, 1] if y is None else y
assert len(x) == len(y)
sizes = sizes if sizes else [len(x)]
logits = constant_op.constant(x, shape=sizes, dtype=dtype, name="logits")
targets = constant_op.constant(y, shape=sizes, dtype=dtype, name="targets")
losses = np.array(self._WeightedCrossEntropy(x, y, q)).reshape(*sizes)
exit((logits, targets, q, losses))
