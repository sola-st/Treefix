# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Makes a 1-D RNG state.

  Args:
    state_size: an integer.
    seed: an integer or 1-D tensor.

  Returns:
    a 1-D tensor of shape [state_size] and dtype STATE_TYPE.
  """
if isinstance(seed, int):
    # chop the Python integer (infinite precision) into chunks of SEED_TYPE
    ls = []
    for _ in range(state_size):
        ls.append(seed & SEED_BIT_MASK)
        seed >>= SEED_TYPE_BITS
    seed = ls
# to avoid overflow error from ops.convert_to_tensor
seed = nest.map_structure(_uint_to_int, seed)
seed = math_ops.cast(seed, STATE_TYPE)
seed = array_ops.reshape(seed, [-1])
seed = seed[0:state_size]
# Padding with zeros on the *left* if too short. Padding on the right would
# cause a small seed to be used as the "counter" while the "key" is always
# zero (for counter-based RNG algorithms), because in the current memory
# layout counter is stored before key. In such a situation two RNGs with
# two different small seeds may generate overlapping outputs.
seed_size = seed.shape[0]
if seed_size is None:
    seed_size = array_ops.shape(seed)[0]
padding_size = math_ops.maximum(state_size - seed_size, 0)
padding = array_ops.zeros([padding_size], seed.dtype)
# can't use `pad` because it doesn't support integer dtypes on GPU
seed = array_ops.concat([padding, seed], axis=0)
seed.set_shape([state_size])
exit(seed)
