# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
variable_strategy = v._distribute_strategy  # pylint: disable=protected-access
if variable_strategy.extended is not extended:
    raise ValueError(
        "`colocate_vars_with` must only be passed a variable created in this "
        "tf.distribute.Strategy.scope(), not %s created in scope: %s" %
        (v, variable_strategy))
