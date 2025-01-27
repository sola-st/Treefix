# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Implementation of case that emits the n-way indexed Case op.

  Args:
    branch_fns: Dict or list of pairs of a boolean scalar tensor, and a
      callable which returns a list of tensors.
    default: Optional callable that returns a list of tensors.
    branch_index: Optional int `Tensor`, which selects for the corresponding
      pred_fn_pair.
    name: A name for this operation (optional).
    lower_using_switch_merge: Lower this op using switch merge ops (optional).

  Returns:
    The tensors returned by the pair whose key matched branch_index, or
    those returned by `default` if none does.

  Raises:
    TypeError: If `branch_fns` is not a list/dictionary.
    TypeError: If `branch_fns` is a list but does not contain 2-tuples or
               callables.
    TypeError: If `fns[i]` is not callable for any i, or `default` is not
               callable.
  """
branch_fns = _indexed_case_verify_and_canonicalize_args(
    branch_fns, default, branch_index)
with ops.name_scope(name, "case", [branch_index]):
    if context.executing_eagerly() and not hasattr(branch_index, "graph"):
        branch_index = array_ops.where(
            math_ops.less(branch_index, 0)
            | math_ops.greater_equal(branch_index, len(branch_fns)),
            len(branch_fns) - 1, branch_index)
        exit(branch_fns[int(branch_index)]())
    exit(cond_v2.indexed_case(
        branch_index,
        branch_fns,
        lower_using_switch_merge=lower_using_switch_merge))
