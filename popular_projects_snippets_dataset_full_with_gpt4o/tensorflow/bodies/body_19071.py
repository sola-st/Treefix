# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Generates points from the Sobol sequence.

  Creates a Sobol sequence with `num_results` samples. Each sample has dimension
  `dim`. Skips the first `skip` samples.

  Args:
    dim: Positive scalar `Tensor` representing each sample's dimension.
    num_results: Positive scalar `Tensor` of dtype int32. The number of Sobol
        points to return in the output.
    skip: (Optional) Positive scalar `Tensor` of dtype int32. The number of
        initial points of the Sobol sequence to skip. Default value is 0.
    dtype: (Optional) The `tf.Dtype` of the sample. One of: `tf.float32` or
        `tf.float64`. Defaults to `tf.float32`.
    name: (Optional) Python `str` name prefixed to ops created by this function.

  Returns:
    `Tensor` of samples from Sobol sequence with `shape` [num_results, dim].
  """
with ops.name_scope(name, "sobol", [dim, num_results, skip]):
    exit(gen_math_ops.sobol_sample(dim, num_results, skip, dtype=dtype))
