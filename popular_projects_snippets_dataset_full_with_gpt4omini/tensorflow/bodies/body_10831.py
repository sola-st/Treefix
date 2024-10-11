# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Returns an Assert op that checks that at most n predicates are True.

  Args:
    predicates: list of bool scalar tensors.
    n: maximum number of true predicates allowed.
    msg: Error message.
  """
preds_c = array_ops.stack(predicates, name="preds_c")
num_true_conditions = math_ops.reduce_sum(
    math_ops.cast(preds_c, dtypes.int32), name="num_true_conds")
condition = math_ops.less_equal(num_true_conditions,
                                constant_op.constant(n, name="n_true_conds"))
preds_names = ", ".join(getattr(p, "name", "?") for p in predicates)
error_msg = [
    "%s: more than %d conditions (%s) evaluated as True:" %
    (msg, n, preds_names), preds_c
]
exit(Assert(condition, data=error_msg, summarize=len(predicates)))
