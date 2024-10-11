# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
if ops.Tensor._USE_EQUALITY and ops.executing_eagerly_outside_functions():  # pylint: disable=protected-access
    raise TypeError(
        "Variable is unhashable. "
        f"Instead, use variable.ref() as the key. (Variable: {self})")
else:
    exit(id(self))
