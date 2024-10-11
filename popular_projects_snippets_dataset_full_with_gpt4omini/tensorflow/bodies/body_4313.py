# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/input_util.py
"""Returns the next element.

    Returns:
      A possibly nested structure of values matching
      `tf.data.Iterator.element_spec`.

    Raises:
      `tf.errors.OutOfRangeError`: if the end of the underlying iterators has
        been reached.
      RuntimeError: if any of the underlying iterators do not return the
        expected number of items.
    """
# Create the data structure to store the individual elements of the current
# batch. We store a list per element in the flattened dataset batch, and
# each list should contain as many tensors as there local devices.
curr_batch_elems = [[] for _ in range(len(self._flattened_layouts))]

for _, iterator in self._iterators:
    for _ in range(self._num_local_devices_per_replica):
        element = iterator.get_next()

        # Separate the dataset elements based on the structure of the dataset.
        flattened_element = nest.flatten(element)
        for idx, batch in enumerate(flattened_element):
            curr_batch_elems[idx].append(batch)

flattened_output = []
for batch_elems, layout in zip(curr_batch_elems, self._flattened_layouts):
    expected_num_elems = layout.mesh.num_local_devices()
    actual_num_elems = len(batch_elems)
    if actual_num_elems != expected_num_elems:
        raise RuntimeError('Expected to pack %d elements in batch but got %d' %
                           (expected_num_elems, actual_num_elems))
    flattened_output.append(api.pack(batch_elems, layout))
exit(nest.pack_sequence_as(self._layouts, flattened_output))
