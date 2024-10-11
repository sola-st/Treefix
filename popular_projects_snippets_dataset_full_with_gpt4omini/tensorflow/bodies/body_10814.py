# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Makes the values known to this context."""
self._values = set()
for x in values:
    if isinstance(x, ops.Tensor):
        self._values.add(x.name)
    else:
        raise TypeError("'values' must be a list of Tensors. "
                        f"Received: {type(x)}.")
