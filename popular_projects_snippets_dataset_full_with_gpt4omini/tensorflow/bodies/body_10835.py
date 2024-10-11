# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Implementation of case that allows for different cond functions.

  Args:
    cond_fn: method that has signature and semantics of `cond` above.
    pred_fn_pairs: Dict or list of pairs of a boolean scalar tensor, and a
      callable which returns a list of tensors.
    default: Optional callable that returns a list of tensors.
    exclusive: True iff at most one predicate is allowed to evaluate to `True`.
    name: A name for this operation (optional).
    allow_python_preds: if true, pred_fn_pairs may contain Python bools in
      addition to boolean Tensors
    **cond_kwargs: keyword arguments that will be passed to `cond_fn`.

  Returns:
    The tensors returned by the first pair whose predicate evaluated to True, or
    those returned by `default` if none does.

  Raises:
    TypeError: If `pred_fn_pairs` is not a list/dictionary.
    TypeError: If `pred_fn_pairs` is a list but does not contain 2-tuples.
    TypeError: If `fns[i]` is not callable for any i, or `default` is not
               callable.
  """
predicates, actions = _case_verify_and_canonicalize_args(
    pred_fn_pairs, exclusive, name, allow_python_preds)
with ops.name_scope(name, "case", [predicates]):
    if default is None:
        default, predicates, actions = _case_create_default_action(
            predicates, actions)
    fn = default
    # To eval conditions in direct order we create nested conditions in reverse:
    #   cond_fn(c[0], true_fn=.., false_fn=cond_fn(c[1], ...))
    for predicate, action in reversed(list(zip(predicates, actions))):
        fn = functools.partial(
            cond_fn, predicate, true_fn=action, false_fn=fn, **cond_kwargs)
    if exclusive:
        with ops.control_dependencies([
            _assert_at_most_n_true(
                predicates, n=1, msg="Input error: exclusive=True")
        ]):
            exit(fn())
    else:
        exit(fn())
