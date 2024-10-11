# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_generator_v1.py
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
