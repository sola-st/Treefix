# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/random_ops.py
"""Outputs random values from a truncated normal distribution.

  The values are drawn from a normal distribution with specified mean and
  standard deviation, discarding and re-drawing any samples that are more than
  two standard deviations from the mean.

  Examples:

  >>> tf.random.truncated_normal(shape=[2])
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([..., ...], dtype=float32)>

  >>> tf.random.truncated_normal(shape=[2], mean=3, stddev=1, dtype=tf.float32)
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([..., ...], dtype=float32)>

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output tensor.
    mean: A 0-D Tensor or Python value of type `dtype`. The mean of the
      truncated normal distribution.
    stddev: A 0-D Tensor or Python value of type `dtype`. The standard deviation
      of the normal distribution, before truncation.
    dtype: The type of the output. Restricted to floating-point types:
      `tf.half`, `tf.float`, `tf.double`, etc.
    seed: A Python integer. Used to create a random seed for the distribution.
      See `tf.random.set_seed` for more information.
    name: A name for the operation (optional).

  Returns:
    A tensor of the specified shape filled with random truncated normal values.
  """
with ops.name_scope(name, "truncated_normal", [shape, mean, stddev]) as name:
    shape_tensor = tensor_util.shape_tensor(shape)
    mean_tensor = ops.convert_to_tensor(mean, dtype=dtype, name="mean")
    stddev_tensor = ops.convert_to_tensor(stddev, dtype=dtype, name="stddev")
    seed1, seed2 = random_seed.get_seed(seed)
    rnd = gen_random_ops.truncated_normal(
        shape_tensor, dtype, seed=seed1, seed2=seed2)
    mul = rnd * stddev_tensor
    value = math_ops.add(mul, mean_tensor, name=name)
    tensor_util.maybe_set_static_shape(value, shape)
    exit(value)
