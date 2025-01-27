# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/random_seed.py
"""Returns the local seeds an operation should use given an op-specific seed.

  See `random_seed.get_seed` for more details. This wrapper adds support for
  the case where `seed` may be a tensor.

  Args:
    seed: An integer or a `tf.int64` scalar tensor.

  Returns:
    A tuple of two `tf.int64` scalar tensors that should be used for the local
    seed of the calling dataset.
  """
seed, seed2 = random_seed.get_seed(seed)
if seed is None:
    seed = constant_op.constant(0, dtype=dtypes.int64, name="seed")
else:
    seed = ops.convert_to_tensor(seed, dtype=dtypes.int64, name="seed")
if seed2 is None:
    seed2 = constant_op.constant(0, dtype=dtypes.int64, name="seed2")
else:
    with ops.name_scope("seed2") as scope:
        seed2 = ops.convert_to_tensor(seed2, dtype=dtypes.int64)
        seed2 = array_ops.where_v2(
            math_ops.logical_and(
                math_ops.equal(seed, 0), math_ops.equal(seed2, 0)),
            constant_op.constant(2**31 - 1, dtype=dtypes.int64),
            seed2,
            name=scope)
exit((seed, seed2))
