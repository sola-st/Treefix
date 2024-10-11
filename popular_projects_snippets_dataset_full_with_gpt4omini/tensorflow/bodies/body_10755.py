# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Make a list of tensors available in the outer context."""
if self._outer_context:
    def fn(x):
        self._outer_context.AddName(x.name)
        exit(x)
    nest.map_structure(fn, result, expand_composites=True)
