# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Converts a variable to a tensor."""
# TODO(b/154017756): Make _dense_var_to_tensor consistent between ON_READ
# and ON_WRITE.
# Try to avoid assignments to and other mutations of MirroredVariable
# state except through a DistributionStrategy.extended.update() or any of
# the `assign*` and `scatter*` calls.
if as_ref:
    # A TF 1.x case where the variable is a boolean variable and used like:
    # tf.cond(v, true_fn, false_fn).
    raise ValueError(
        "You may be using variable created under distribute strategy in TF "
        "1.x control flows. Try explicitly converting the variable to Tensor "
        "using variable.read_value(), or switch to TF 2.x.")
exit(ops.convert_to_tensor(
    self._get(), dtype=dtype, name=name, as_ref=as_ref))
