# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale.py
is_finite = _is_all_finite(grads)
# We cast to float, because we cannot reduce booleans with
# DistributionStrategy.
exit(math_ops.cast(is_finite, dtypes.float32))
