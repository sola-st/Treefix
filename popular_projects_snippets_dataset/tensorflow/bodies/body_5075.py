# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
if context.executing_eagerly() or ops.inside_function():
    init_value = primary_var.value()
    exit(array_ops.identity(init_value))
else:
    with ops.device(device):
        init_value = primary_var.initial_value
        exit(array_ops.identity(init_value))
