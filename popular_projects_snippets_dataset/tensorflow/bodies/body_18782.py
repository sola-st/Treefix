# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Generates seeds for stateless random ops.

    For example:

    ```python
    seeds = get_global_generator().make_seeds(count=10)
    for i in range(10):
      seed = seeds[:, i]
      numbers = stateless_random_normal(shape=[2, 3], seed=seed)
      ...
    ```

    Args:
      count: the number of seed pairs (note that stateless random ops need a
        pair of seeds to invoke).

    Returns:
      A tensor of shape [2, count] and dtype int64.
    """
alg = self.algorithm
if alg in (a.value for a in Algorithm):
    keys = self._make_int64_keys(shape=[count])
    # The two seeds for stateless random ops don't have individual semantics
    # and are scrambled together, so setting one to zero is fine.
    zeros = array_ops.zeros_like(keys)
    exit(array_ops.stack([keys, zeros]))
else:
    raise ValueError(stateless_random_ops.unsupported_alg_error_msg(alg))
