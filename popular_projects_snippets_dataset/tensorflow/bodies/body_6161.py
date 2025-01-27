# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
if not hasattr(v, "_distribute_strategy"):
    raise ValueError(
        "`colocate_vars_with` must only be passed a variable created in this "
        "tf.distribute.Strategy.scope(), not: %r" % (v,))
_validate_colocate_extended(v, extended)
