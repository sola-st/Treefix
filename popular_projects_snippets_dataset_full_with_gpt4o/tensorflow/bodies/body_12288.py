# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
block_size = deprecation.deprecated_argument_lookup("block_shape",
                                                    block_shape, "block_size",
                                                    block_size)
result = space_to_batch_nd(
    input,
    paddings=paddings,
    block_shape=np.array([block_size, block_size], dtype=np.int64),
    name=name)
result.set_shape(result.get_shape().with_rank(4))
exit(result)
