# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Outputs random values from a binomial distribution.

    The generated values follow a binomial distribution with specified count and
    probability of success parameters.

    Example:

    ```python
    counts = [10., 20.]
    # Probability of success.
    probs = [0.8]

    rng = tf.random.Generator.from_seed(seed=234)
    binomial_samples = rng.binomial(shape=[2], counts=counts, probs=probs)


    counts = ... # Shape [3, 1, 2]
    probs = ...  # Shape [1, 4, 2]
    shape = [3, 4, 3, 4, 2]
    rng = tf.random.Generator.from_seed(seed=1717)
    # Sample shape will be [3, 4, 3, 4, 2]
    binomial_samples = rng.binomial(shape=shape, counts=counts, probs=probs)
    ```


    Args:
      shape: A 1-D integer Tensor or Python array. The shape of the output
        tensor.
      counts: Tensor. The counts of the binomial distribution. Must be
        broadcastable with `probs`, and broadcastable with the rightmost
        dimensions of `shape`.
      probs: Tensor. The probability of success for the
        binomial distribution. Must be broadcastable with `counts` and
        broadcastable with the rightmost dimensions of `shape`.
      dtype: The type of the output. Default: tf.int32
      name: A name for the operation (optional).

    Returns:
      samples: A Tensor of the specified shape filled with random binomial
        values.  For each i, each samples[i, ...] is an independent draw from
        the binomial distribution on counts[i] trials with probability of
        success probs[i].
    """
dtype = dtypes.as_dtype(dtype)
with ops.name_scope(name, "binomial", [shape, counts, probs]) as name:
    counts = ops.convert_to_tensor(counts, name="counts")
    probs = ops.convert_to_tensor(probs, name="probs")
    shape_tensor = _shape_tensor(shape)
    exit(gen_stateful_random_ops.stateful_random_binomial(
        self.state.handle,
        self.algorithm,
        shape=shape_tensor,
        counts=counts,
        probs=probs,
        dtype=dtype,
        name=name))
