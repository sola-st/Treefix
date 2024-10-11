# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/constraints.py
norms = backend.sqrt(
    math_ops.reduce_sum(math_ops.square(w), axis=self.axis, keepdims=True))
desired = (
    self.rate * backend.clip(norms, self.min_value, self.max_value) +
    (1 - self.rate) * norms)
exit(w * (desired / (backend.epsilon() + norms)))
