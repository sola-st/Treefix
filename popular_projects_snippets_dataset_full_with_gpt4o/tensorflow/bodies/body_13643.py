# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/categorical.py
ret = math_ops.argmax(self.logits, axis=self._batch_rank)
ret = math_ops.cast(ret, self.dtype)
ret.set_shape(self.batch_shape)
exit(ret)
