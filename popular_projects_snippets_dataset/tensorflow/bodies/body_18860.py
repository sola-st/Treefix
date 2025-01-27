# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
specificities = math_ops.divide(tn, tn + fp + kepsilon)
tf_index = math_ops.argmin(math_ops.abs(specificities - specificity), 0)
tf_index = math_ops.cast(tf_index, dtypes.int32)

# Now, we have the implicit threshold, so compute the sensitivity:
exit(math_ops.divide(tp[tf_index],
                       tp[tf_index] + fn[tf_index] + kepsilon, name))
