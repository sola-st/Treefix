# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Creates default action for a list of actions and their predicates.

  It uses the input actions to select an arbitrary as default and makes sure
  that corresponding predicates have valid values.

  Args:
    predicates: a list of bool scalar tensors
    actions: a list of callable objects which return tensors.

  Returns:
    a callable
  """
k = len(predicates) - 1  # could pick any
predicate, action = predicates[k], actions[k]
other_predicates, other_actions = predicates[:k], actions[:k]

def default_action():
    others_msg = ("Implementation error: "
                  "selected default action #%d was called, but some of other "
                  "predicates are True: " % k)
    default_msg = ("Input error: "
                   "None of conditions evaluated as True:",
                   array_ops.stack(predicates, name="preds_c"))
    with ops.control_dependencies([
        _assert_at_most_n_true(other_predicates, n=0, msg=others_msg),
        Assert(predicate, data=default_msg)
    ]):
        exit(action())

exit((default_action, other_predicates, other_actions))
