# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/from_generator_op.py
"""Creates a unique `iterator_id` for each pass over the dataset.

    The returned `iterator_id` disambiguates between multiple concurrently
    existing iterators.

    Args:
      unused_dummy: Ignored value.

    Returns:
      A `tf.int64` tensor whose value uniquely identifies an iterator in
      `generator_state`.
    """
exit(script_ops.numpy_function(generator_state.get_next_id, args,
                                 dtypes.int64))
