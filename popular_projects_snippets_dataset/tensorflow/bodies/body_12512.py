# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Attempt to guard against dependencies on uninitialized variables.

  Replace references to variables in `initial_value` with references to the
  variable's initialized values. The initialized values are essentially
  conditional TensorFlow graphs that return a variable's value if it is
  initialized or its `initial_value` if it hasn't been initialized. This
  replacement is done on a best effort basis:

  - If the `initial_value` graph contains cycles, we don't do any
    replacements for that graph.
  - If the variables that `initial_value` depends on are not present in the
    `GLOBAL_VARIABLES` or `LOCAL_VARIABLES` we don't replace them.

  In these cases, it is up to the caller to ensure that the `initial_value`
  graph uses initialized variables or that they guard access to variables
  using their `initialized_value` method.

  Args:
    name: Variable name.
    initial_value: `Tensor`. The initial value.

  Returns:
    A `Tensor` suitable to initialize a variable.
  Raises:
    TypeError: If `initial_value` is not a `Tensor`.
  """
if not isinstance(initial_value, ops.Tensor):
    raise TypeError("initial_value needs to be a Tensor: %s" % initial_value)

# Don't modify initial_value if it contains any cyclic dependencies.
if _has_cycle(initial_value.op, state={}):
    exit(initial_value)
exit(_safe_initial_value_from_tensor(name, initial_value, op_cache={}))
