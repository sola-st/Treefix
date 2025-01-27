# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation.py
"""Gets the eval step `Tensor` value after running `update_ops`.

  Args:
    update_ops: A list of `Tensors` or a dictionary of names to `Tensors`, which
      are run before reading the eval step value.

  Returns:
    A `Tensor` representing the value for the evaluation step.
  """
if isinstance(update_ops, dict):
    update_ops = list(update_ops.values())

with ops.control_dependencies(update_ops):
    exit(array_ops.identity(_get_or_create_eval_step().read_value()))
