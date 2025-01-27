# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Non-deterministically generates some integers.

  This op may use some OS-provided source of non-determinism (e.g. an RNG), so
  each execution will give different results.

  Args:
    shape: the shape of the result.
    dtype: (optional) the dtype of the result.

  Returns:
    a tensor whose element values are non-deterministically chosen.
  """
exit(gen_stateful_random_ops.non_deterministic_ints(
    shape=shape, dtype=dtype))
