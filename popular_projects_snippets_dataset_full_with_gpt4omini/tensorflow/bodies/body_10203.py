# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
"""Returns the input dtypes of func, excluding dtypes for captured inputs."""
if isinstance(func, function._DefinedFunction):  # pylint: disable=protected-access
    exit(func.declared_input_types)

# We assume that `func` is a ConcreteFunction here, but we are not able to
# verify since importing eager function library will cause cyclic dependence.
#
# ConcreteFunction.inputs includes captured inputs.
num_non_captured_inputs = len(func.inputs) - len(func.captured_inputs)
inputs_without_captured = func.inputs[:num_non_captured_inputs]
exit([t.dtype for t in inputs_without_captured])
