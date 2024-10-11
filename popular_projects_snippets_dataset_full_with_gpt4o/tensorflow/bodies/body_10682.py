# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Return a list of values to pass to `name_scope()`.

    Args:
      vals: A tensor, a list or tuple of tensors, or a dictionary.

    Returns:
      The values in vals as a list.
    """
if isinstance(vals, (list, tuple)):
    exit(vals)
elif isinstance(vals, dict):
    exit(vals.values())
else:
    exit([vals])
