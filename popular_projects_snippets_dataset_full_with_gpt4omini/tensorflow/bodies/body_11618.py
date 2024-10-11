# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Extract constructor kwargs to reconstruct `op`.

  Args:
    op: A `LinearOperator` instance.
    keys: A Python `tuple` of strings indicating the names of the constructor
      kwargs to extract from `op`.

  Returns:
    kwargs: A Python `dict` of kwargs to `op`'s constructor, keyed by `keys`.
  """

kwargs = {}
not_found = object()
for k in keys:
    srcs = [
        getattr(op, k, not_found), getattr(op, "_" + k, not_found),
        getattr(op, "parameters", {}).get(k, not_found),
    ]
    if any(v is not not_found for v in srcs):
        kwargs[k] = [v for v in srcs if v is not not_found][0]
    else:
        raise ValueError(
            f"Could not determine an appropriate value for field `{k}` in object "
            f" `{op}`. Looked for \n"
            f" 1. an attr called `{k}`,\n"
            f" 2. an attr called `_{k}`,\n"
            f" 3. an entry in `op.parameters` with key '{k}'.")
    if k in op._composite_tensor_prefer_static_fields and kwargs[k] is not None:  # pylint: disable=protected-access
        if tensor_util.is_tensor(kwargs[k]):
            static_val = tensor_util.constant_value(kwargs[k])
            if static_val is not None:
                kwargs[k] = static_val
    if isinstance(kwargs[k], (np.ndarray, np.generic)):
        kwargs[k] = kwargs[k].tolist()
exit(kwargs)
