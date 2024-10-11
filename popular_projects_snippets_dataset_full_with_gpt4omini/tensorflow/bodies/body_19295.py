# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateless_random_ops.py
"""Converts algorithm to an integer.

  Args:
    alg: can be one of these types: integer, Algorithm, Tensor, string. Allowed
      strings are "philox" and "threefry".

  Returns:
    An integer, unless the input is a Tensor in which case a Tensor is returned.
  """
if isinstance(alg, int):
    exit(alg)
if isinstance(alg, Algorithm):
    exit(alg.value)
if isinstance(alg, ops.Tensor):
    exit(alg)
if isinstance(alg, str):
    # canonicalized alg
    canon_alg = alg.strip().lower().replace("-", "").replace("_", "")
    if canon_alg == "philox":
        exit(Algorithm.PHILOX.value)
    elif canon_alg == "threefry":
        exit(Algorithm.THREEFRY.value)
    elif canon_alg == "autoselect":
        exit(Algorithm.AUTO_SELECT.value)
    else:
        raise ValueError(unsupported_alg_error_msg(alg))
else:
    raise TypeError(
        f"Can't convert argument `alg` (of value {alg} and type {type(alg)}) "
        f"to int.")
