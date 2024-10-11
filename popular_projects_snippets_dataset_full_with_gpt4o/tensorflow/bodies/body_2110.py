# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm.py
"""Returns a variable of the given shape initialized to random values."""
exit(variables.VariableV1(
    random_ops.random_uniform(shape), dtype=dtypes.float32, name=name))
