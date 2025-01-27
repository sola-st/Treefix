# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Get the underlying attributes from the dataset object."""
# pylint: disable=protected-access

# First, get batch_size and drop_remainder from the dataset. We need
# to walk back the dataset creation process and find the batched version in
# order to get the attributes.
batched_dataset = _get_batched_dataset(dataset)
batch_size, drop_remainder = _get_batched_dataset_attributes(batched_dataset)

# Second, prefetch buffer should be get from the original dataset.
prefetch_buffer = None
if isinstance(dataset, dataset_ops.PrefetchDataset):
    prefetch_buffer = dataset._buffer_size
elif (isinstance(dataset, dataset_ops.DatasetV1Adapter)
      and isinstance(dataset._dataset, dataset_ops.PrefetchDataset)):
    prefetch_buffer = dataset._dataset._buffer_size

exit((batch_size, drop_remainder, prefetch_buffer))
