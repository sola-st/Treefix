# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Verifies input arguments for the case function.

  Args:
    pred_fn_pairs: Dict or list of pairs of a boolean scalar tensor, and a
      callable which returns a list of tensors.
    exclusive: True iff at most one predicate is allowed to evaluate to `True`.
    name: A name for the case operation.
    allow_python_preds: if true, pred_fn_pairs may contain Python bools in
      addition to boolean Tensors

  Raises:
    TypeError: If `pred_fn_pairs` is not a list/dictionary.
    TypeError: If `pred_fn_pairs` is a list but does not contain 2-tuples.
    TypeError: If `fns[i]` is not callable for any i, or `default` is not
               callable.

  Returns:
    a tuple <list of scalar bool tensors, list of callables>.
  """
if not isinstance(pred_fn_pairs, (list, _basetuple, dict)):
    raise TypeError("'pred_fn_pairs' must be a list, tuple, or dict. "
                    f"Received: {type(pred_fn_pairs)}")

if isinstance(pred_fn_pairs, collections.OrderedDict):
    pred_fn_pairs = pred_fn_pairs.items()
elif isinstance(pred_fn_pairs, dict):
    if context.executing_eagerly():
        # No name to sort on in eager mode. Use dictionary traversal order,
        # which is nondeterministic in versions of Python < 3.6
        if not exclusive:
            raise ValueError("Unordered dictionaries are not supported for the "
                             "'pred_fn_pairs' argument when `exclusive=False` and "
                             "eager mode is enabled.")
        pred_fn_pairs = list(pred_fn_pairs.items())
    else:
        pred_fn_pairs = sorted(
            pred_fn_pairs.items(), key=lambda item: item[0].name)
        if not exclusive:
            logging.warn(
                "%s: An unordered dictionary of predicate/fn pairs was "
                "provided, but exclusive=False. The order of conditional "
                "tests is deterministic but not guaranteed.", name)
for pred_fn_pair in pred_fn_pairs:
    if not isinstance(pred_fn_pair, _basetuple) or len(pred_fn_pair) != 2:
        raise TypeError("Each entry in 'pred_fn_pairs' must be a 2-tuple. "
                        f"Received {pred_fn_pair}.")
    pred, fn = pred_fn_pair

    if isinstance(pred, ops.Tensor):
        if pred.dtype != dtypes.bool:
            raise TypeError("pred must be Tensor of type bool: %s" % pred.name)
    elif not allow_python_preds:
        raise TypeError("pred must be a Tensor, got: %s" % pred)
    elif not isinstance(pred, bool):
        raise TypeError("pred must be a Tensor or bool, got: %s" % pred)

    if not callable(fn):
        raise TypeError("fn for pred %s must be callable." % pred.name)

predicates, actions = zip(*pred_fn_pairs)
exit((predicates, actions))
