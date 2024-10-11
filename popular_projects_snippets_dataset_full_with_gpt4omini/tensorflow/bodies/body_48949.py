# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Sets self._dtype_policy."""
if isinstance(dtype, policy.Policy):
    self._dtype_policy = dtype
elif isinstance(dtype, dict):
    self._dtype_policy = policy.deserialize(dtype)
elif isinstance(dtype, str) and dtype in ('mixed_float16',
                                          'mixed_bfloat16'):
    # The isinstance check is required since np.dtype raises an error if
    # compared to a non-dtype string.
    self._dtype_policy = policy.Policy(dtype)
elif dtype:
    self._dtype_policy = policy.Policy(dtypes.as_dtype(dtype).name)
else:
    self._dtype_policy = policy.global_policy()
if (self._dtype_policy.name == 'mixed_float16' and
    not loss_scale_optimizer.strategy_supports_loss_scaling()):
    # Although only loss scaling doesn't support certain strategies, to avoid
    # confusion, we disallow the 'mixed_float16' policy with unsupported
    # strategies. This is because 'mixed_float16' requires loss scaling for
    # numeric stability.
    strategy = ds_context.get_strategy()
    raise ValueError('Mixed precision is not supported with the '
                     'tf.distribute.Strategy: %s. Either stop using mixed '
                     'precision by removing the use of the "%s" policy or '
                     'use a different Strategy, e.g. a MirroredStrategy.' %
                     (strategy.__class__.__name__, self._dtype_policy.name))

# Performance optimization: cache the compute dtype as a Dtype object or
# None, so that str to Dtype conversion doesn't happen in Layer.__call__.
# TODO(b/157486353): Investigate returning DTypes in Policy.
if self._dtype_policy.compute_dtype:
    self._compute_dtype_object = dtypes.as_dtype(
        self._dtype_policy.compute_dtype)
else:
    self._compute_dtype_object = None
