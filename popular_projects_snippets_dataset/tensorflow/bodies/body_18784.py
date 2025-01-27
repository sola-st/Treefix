# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Returns a list of independent `Generator` objects.

    Two generators are independent of each other in the sense that the
    random-number streams they generate don't have statistically detectable
    correlations. The new generators are also independent of the old one.
    The old generator's state will be changed (like other random-number
    generating methods), so two calls of `split` will return different
    new generators.

    For example:

    ```python
    gens = get_global_generator().split(count=10)
    for gen in gens:
      numbers = gen.normal(shape=[2, 3])
      # ...
    gens2 = get_global_generator().split(count=10)
    # gens2 will be different from gens
    ```

    The new generators will be put on the current device (possible different
    from the old generator's), for example:

    ```python
    with tf.device("/device:CPU:0"):
      gen = Generator(seed=1234)  # gen is on CPU
    with tf.device("/device:GPU:0"):
      gens = gen.split(count=10)  # gens are on GPU
    ```

    Args:
      count: the number of generators to return.

    Returns:
      A list (length `count`) of `Generator` objects independent of each other.
      The new generators have the same RNG algorithm as the old one.
    """
def _key_to_state(alg, key):
    # Padding with zeros on the left. The zeros will be the counter.
    exit([0] * (_get_state_size(alg) - 1) + [key])

alg = self.algorithm
if alg in (a.value for a in Algorithm):
    keys = self._make_int64_keys(shape=[count])
    exit([Generator(state=_key_to_state(alg, key), alg=alg)
            for key in array_ops.unstack(keys, num=count)])
else:
    raise ValueError(stateless_random_ops.unsupported_alg_error_msg(alg))
