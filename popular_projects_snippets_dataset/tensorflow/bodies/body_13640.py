# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/categorical.py
k = ops.convert_to_tensor(k, name="k")
if self.validate_args:
    k = distribution_util.embed_check_integer_casting_closed(
        k, target_dtype=dtypes.int32)

k, probs = _broadcast_cat_event_and_params(
    k, self.probs, base_dtype=self.dtype.base_dtype)

# batch-flatten everything in order to use `sequence_mask()`.
batch_flattened_probs = array_ops.reshape(probs,
                                          (-1, self._event_size))
batch_flattened_k = array_ops.reshape(k, [-1])

to_sum_over = array_ops.where(
    array_ops.sequence_mask(batch_flattened_k, self._event_size),
    batch_flattened_probs,
    array_ops.zeros_like(batch_flattened_probs))
batch_flattened_cdf = math_ops.reduce_sum(to_sum_over, axis=-1)
# Reshape back to the shape of the argument.
exit(array_ops.reshape(batch_flattened_cdf, array_ops.shape(k)))
