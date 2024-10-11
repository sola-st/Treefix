# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Verifies input arguments for the case function.

  Args:
    branch_fns: Dict or list of pairs of an `int` and a callable which
      returns a list of tensors.
    default: Optional callable that returns a list of tensors.
    branch_index: Optional int `Tensor`, which selects for the corresponding
      pred_fn_pair.

  Raises:
    TypeError: If `branch_fns` is not a list/dictionary.
    TypeError: If `branch_fns` is a list but does not contain 2-tuples or
               callables.
    TypeError: If `fns[i]` is not callable for any i, or `default` is not
               callable.

  Returns:
    branch_fns: validated list of callables for each branch (default last).
  """
if not isinstance(branch_index, ops.Tensor):
    raise TypeError("'branch_index' must be a Tensor, got {}".format(
        type(branch_index)))
if not branch_index.dtype.is_integer:
    raise TypeError("'branch_index' must be an integer Tensor, got {}".format(
        branch_index.dtype))

if not branch_fns:
    raise ValueError("Must provide at least one item in 'branch_fns'")
if not isinstance(branch_fns, (list, _basetuple, dict)):
    raise TypeError("'branch_fns' must be a list, tuple, or dict")

if isinstance(branch_fns, dict):
    branch_fns = branch_fns.items()

if all(callable(fn) for fn in branch_fns):
    branch_fns = list(enumerate(branch_fns))

for key_fn_pair in branch_fns:
    if not isinstance(key_fn_pair, _basetuple) or len(key_fn_pair) != 2:
        raise TypeError("Each entry in 'branch_fns' must be a 2-tuple. "
                        f"Received {key_fn_pair}.")
    key, branch_fn = key_fn_pair

    if not isinstance(key, int):
        raise TypeError("key must be a Python `int`, got {}".format(type(key)))

    if not callable(branch_fn):
        raise TypeError("fn for key {} must be callable.".format(key))

keys = [p[0] for p in branch_fns]
if min(keys) < 0 or max(keys) >= len(keys) or len(set(keys)) != len(keys):
    raise ValueError(
        "branch indices (keys) must form contiguous range of [0 to {}) but "
        "found {{{}}}".format(len(keys), ",".join(map(str, sorted(keys)))))
actions = [p[1] for p in sorted(branch_fns)]
if default is not None:
    actions.append(default)
exit(actions)
