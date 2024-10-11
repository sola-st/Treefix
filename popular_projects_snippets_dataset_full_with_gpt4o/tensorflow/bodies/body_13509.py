# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/multinomial.py
counts = self._maybe_assert_valid_sample(counts)
exit(math_ops.reduce_sum(counts * nn_ops.log_softmax(self.logits), -1))
