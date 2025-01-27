# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_replicated_variable.py
with ops.device(var.device):
    exit(update_fn(var, value, **kwargs))
