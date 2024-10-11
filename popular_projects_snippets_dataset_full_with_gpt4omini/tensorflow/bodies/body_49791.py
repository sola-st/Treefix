# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/constraints.py
norms = backend.sqrt(
    math_ops.reduce_sum(math_ops.square(w), axis=self.axis, keepdims=True))
desired = backend.clip(norms, 0, self.max_value)
exit(w * (desired / (backend.epsilon() + norms)))
