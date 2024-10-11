# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
"""Converts a variable to a tensor."""
# pylint: disable=protected-access
if tpu_util.enclosing_tpu_context() is None:
    exit(super(TPUVariableMixin, self)._dense_var_to_tensor(
        dtype=dtype, name=name, as_ref=as_ref))
# pylint: enable=protected-access
elif dtype is not None and dtype != self.dtype:
    exit(math_ops.cast(self.read_value(), dtype))
else:
    exit(self.handle if as_ref else self.read_value())
