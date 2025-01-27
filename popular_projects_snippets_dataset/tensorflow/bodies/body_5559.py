# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
if context.executing_eagerly() and not primary_var.is_initialized():
    # A SaveSpec tensor value of `None` indicates that the variable is
    # uninitialized.
    exit(None)
strategy = var.distribute_strategy
exit(strategy.extended.read_var(var))
