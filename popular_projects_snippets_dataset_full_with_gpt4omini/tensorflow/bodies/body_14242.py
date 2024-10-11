# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/random_ops.py
"""Outputs random values from a truncated normal distribution.

  The generated values follow a normal distribution with specified mean and
  standard deviation, except that values whose magnitude is more than 2 standard
  deviations from the mean are dropped and re-picked.

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output tensor.
    means: A 0-D Tensor or Python value of type `dtype`. The mean of the
      truncated normal distribution.
    stddevs: A 0-D Tensor or Python value of type `dtype`. The standard
      deviation of the truncated normal distribution.
    minvals: A 0-D Tensor or Python value of type `dtype`. The minimum value of
      the truncated normal distribution.
    maxvals: A 0-D Tensor or Python value of type `dtype`. The maximum value of
      the truncated normal distribution.
    dtype: The type of the output.
    seed: A Python integer. Used to create a random seed for the distribution.
      See
      `tf.random.set_seed`
      for behavior.
    name: A name for the operation (optional).

  Returns:
    A tensor of the specified shape filled with random truncated normal values.
  """
with ops.name_scope(name, "parameterized_truncated_normal",
                    [shape, means, stddevs, minvals, maxvals]) as name:
    shape_tensor = tensor_util.shape_tensor(shape)
    means_tensor = ops.convert_to_tensor(means, dtype=dtype, name="means")
    stddevs_tensor = ops.convert_to_tensor(stddevs, dtype=dtype, name="stddevs")
    minvals_tensor = ops.convert_to_tensor(minvals, dtype=dtype, name="minvals")
    maxvals_tensor = ops.convert_to_tensor(maxvals, dtype=dtype, name="maxvals")
    seed1, seed2 = random_seed.get_seed(seed)
    rnd = gen_random_ops.parameterized_truncated_normal(
        shape_tensor,
        means_tensor,
        stddevs_tensor,
        minvals_tensor,
        maxvals_tensor,
        seed=seed1,
        seed2=seed2)
    tensor_util.maybe_set_static_shape(rnd, shape)
    exit(rnd)
