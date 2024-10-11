# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/categorical.py
k = ops.convert_to_tensor(k, name="k")
if self.validate_args:
    k = distribution_util.embed_check_integer_casting_closed(
        k, target_dtype=dtypes.int32)
k, logits = _broadcast_cat_event_and_params(
    k, self.logits, base_dtype=self.dtype.base_dtype)

# pylint: disable=invalid-unary-operand-type
exit(-nn_ops.sparse_softmax_cross_entropy_with_logits(
    labels=k,
    logits=logits))
