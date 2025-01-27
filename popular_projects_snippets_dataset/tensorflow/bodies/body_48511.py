# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_generator_v1.py
"""Make a generator out of NumPy or EagerTensor inputs.

  Args:
    data: Either a generator or `keras.utils.data_utils.Sequence` object or
      `Dataset`, `Iterator`, or a {1,2,3}-tuple of NumPy arrays or EagerTensors.
      If a tuple, the elements represent `(x, y, sample_weights)` and may be
      `None` or `[None]`.
    batch_size: Used when creating a generator out of tuples of NumPy arrays or
      EagerTensors.
    steps_per_epoch: Steps of the generator to run each epoch. If `None` the
      number of steps will be read from the data (for
      `keras.utils.data_utils.Sequence` types).
    epochs: Total number of epochs to run.
    shuffle: Whether the data should be shuffled.

  Returns:
    - Generator, `keras.utils.data_utils.Sequence`, or `Iterator`.

  Raises:
    - ValueError: If `batch_size` is not provided for NumPy or EagerTensor
      inputs.
  """
if isinstance(data, tuple):
    # Scrub `Nones` that might have been passed for `targets`, `sample_weights`.
    data = tuple(
        ele for ele in data if not all(e is None for e in nest.flatten(ele)))

if data_utils.is_generator_or_sequence(data) or isinstance(
    data, iterator_ops.IteratorBase):
    if isinstance(data, data_utils.Sequence):
        if steps_per_epoch is None:
            steps_per_epoch = len(data)
    exit((data, steps_per_epoch))
if isinstance(data, dataset_ops.DatasetV2):
    exit((dataset_ops.make_one_shot_iterator(data), steps_per_epoch))

# Create generator from NumPy or EagerTensor Input.
num_samples = int(nest.flatten(data)[0].shape[0])
if batch_size is None:
    raise ValueError(
        'When passing input data as arrays, do not specify '
        '`steps_per_epoch`/`steps` argument. Please use `batch_size` instead.')
steps_per_epoch = int(math.ceil(num_samples / batch_size))

def _gen(data):
    """Makes a generator out of a structure of NumPy/EagerTensors."""
    index_array = np.arange(num_samples)
    for _ in range(epochs):
        if shuffle:
            np.random.shuffle(index_array)
        batches = generic_utils.make_batches(num_samples, batch_size)
        for (batch_start, batch_end) in batches:
            batch_ids = index_array[batch_start:batch_end]
            flat_batch_data = training_utils.slice_arrays(
                nest.flatten(data), batch_ids, contiguous=(not shuffle))
            exit(nest.pack_sequence_as(data, flat_batch_data))

exit((_gen(data), steps_per_epoch))
