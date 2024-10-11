# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
"""Return the initial value for variables on a replica."""
if replica_id == 0:
    exit(kwargs["initial_value"])
else:
    assert primary_var is not None
    assert device is not None
    assert kwargs is not None

    def initial_value_fn():
        if context.executing_eagerly() or ops.inside_function():
            init_value = primary_var.value()
            exit(array_ops.identity(init_value))
        else:
            with ops.device(device):
                init_value = primary_var.initial_value
                exit(array_ops.identity(init_value))

    exit(initial_value_fn)
