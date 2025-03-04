# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateless_random_ops.py
"""Outputs deterministic pseudorandom values from a normal distribution.

  This is a stateless version of `tf.random.normal`: if run twice with the
  same seeds and shapes, it will produce the same pseudorandom numbers.  The
  output is consistent across multiple runs on the same hardware (and between
  CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU
  hardware.

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output tensor.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
    mean: A 0-D Tensor or Python value of type `dtype`. The mean of the normal
      distribution.
    stddev: A 0-D Tensor or Python value of type `dtype`. The standard deviation
      of the normal distribution.
    dtype: The float type of the output: `float16`, `bfloat16`, `float32`,
      `float64`. Defaults to `float32`.
    name: A name for the operation (optional).
    alg: The RNG algorithm used to generate the random numbers. See
      `tf.random.stateless_uniform` for a detailed explanation.

  Returns:
    A tensor of the specified shape filled with random normal values.
  """
with ops.name_scope(name, "stateless_random_normal",
                    [shape, seed, mean, stddev]) as name:
    shape = tensor_util.shape_tensor(shape)
    mean = ops.convert_to_tensor(mean, dtype=dtype, name="mean")
    stddev = ops.convert_to_tensor(stddev, dtype=dtype, name="stddev")
    key, counter, alg = _get_key_counter_alg(seed, alg)
    rnd = gen_stateless_random_ops_v2.stateless_random_normal_v2(
        shape, key=key, counter=counter, dtype=dtype, alg=alg)
    result = math_ops.add(rnd * stddev, mean, name=name)
    tensor_util.maybe_set_static_shape(result, shape)
    exit(result)
