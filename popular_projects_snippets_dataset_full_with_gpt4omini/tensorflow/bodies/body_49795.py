# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/constraints.py
exit(w / (
    backend.epsilon() + backend.sqrt(
        math_ops.reduce_sum(
            math_ops.square(w), axis=self.axis, keepdims=True))))
