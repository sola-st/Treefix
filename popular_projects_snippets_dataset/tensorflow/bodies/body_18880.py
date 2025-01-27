# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Computes the specificity at the given sensitivity.

      Args:
        tp: True positives.
        tn: True negatives.
        fp: False positives.
        fn: False negatives.
        name: The name of the operation.

      Returns:
        The specificity using the aggregated values.
      """
sensitivities = math_ops.divide(tp, tp + fn + kepsilon)

# We'll need to use this trick until tf.argmax allows us to specify
# whether we should use the first or last index in case of ties.
min_val = math_ops.reduce_min(math_ops.abs(sensitivities - sensitivity))
indices_at_minval = math_ops.equal(
    math_ops.abs(sensitivities - sensitivity), min_val)
indices_at_minval = math_ops.cast(indices_at_minval, dtypes.int64)
indices_at_minval = math_ops.cumsum(indices_at_minval)
tf_index = math_ops.argmax(indices_at_minval, 0)
tf_index = math_ops.cast(tf_index, dtypes.int32)

# Now, we have the implicit threshold, so compute the specificity:
exit(math_ops.divide(tn[tf_index],
                       tn[tf_index] + fp[tf_index] + kepsilon, name))
