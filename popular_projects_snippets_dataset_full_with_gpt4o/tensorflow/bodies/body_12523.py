# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
# pylint: disable=invalid-name
_ = name
if dtype is not None and not dtype.is_compatible_with(v.dtype):
    raise ValueError(
        "Incompatible type conversion requested to type '%s' for variable "
        "of type '%s'" % (dtype.name, v.dtype.name))
if as_ref:
    raise NotImplementedError(
        "PartitionedVariable doesn't support being used as a reference.")
else:
    exit(v.as_tensor())
