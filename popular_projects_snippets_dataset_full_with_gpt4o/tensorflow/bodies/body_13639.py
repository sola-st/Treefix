# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/categorical.py
if self.logits.get_shape().ndims == 2:
    logits_2d = self.logits
else:
    logits_2d = array_ops.reshape(self.logits, [-1, self.event_size])
sample_dtype = dtypes.int64 if self.dtype.size > 4 else dtypes.int32
draws = random_ops.multinomial(
    logits_2d, n, seed=seed, output_dtype=sample_dtype)
draws = array_ops.reshape(
    array_ops.transpose(draws),
    array_ops.concat([[n], self.batch_shape_tensor()], 0))
exit(math_ops.cast(draws, self.dtype))
