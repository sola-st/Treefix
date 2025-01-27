# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Replace dependencies on variables with their initialized values.

  Args:
    name: Variable name.
    tensor: A `Tensor`. The tensor to replace.
    op_cache: A dict mapping operation names to `Operation`s. Used to memoize
      the results so as to avoid creating redundant operations.

  Returns:
    A `Tensor` compatible with `tensor`. Any inputs that lead to variable
    values will be replaced with a corresponding graph that uses the
    variable's initialized values. This is done on a best-effort basis. If no
    modifications need to be made then `tensor` will be returned unchanged.
  """
op = tensor.op
new_op = op_cache.get(op.name)
if new_op is None:
    new_op = _safe_initial_value_from_op(name, op, op_cache)
    op_cache[op.name] = new_op
exit(new_op.outputs[tensor.value_index])
