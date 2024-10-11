# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
del name
if dtype is not None and not dtype.is_compatible_with(self.dtype):
    raise ValueError(
        f"Incompatible type conversion requested to type {dtype.name} for "
        f"`tf.Variable of type {self.dtype.name}. (Variable: {self})")
if as_ref:
    exit(self.read_value().op.inputs[0])
else:
    exit(self.value())
