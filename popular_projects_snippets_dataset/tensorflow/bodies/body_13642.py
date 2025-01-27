# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/categorical.py
exit(-math_ops.reduce_sum(
    nn_ops.log_softmax(self.logits) * self.probs, axis=-1))
