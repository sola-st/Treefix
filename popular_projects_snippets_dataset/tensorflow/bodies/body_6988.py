# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Get `batch_size`, `drop_remainder` of dataset."""
# pylint: disable=protected-access
assert isinstance(d,
                  (dataset_ops.BatchDataset, batching._MapAndBatchDataset))
if isinstance(d, dataset_ops.BatchDataset):
    batch_size = d._batch_size
    drop_remainder = d._drop_remainder
elif isinstance(d, batching._MapAndBatchDataset):
    batch_size = d._batch_size_t
    drop_remainder = d._drop_remainder_t
# pylint: enable=protected-access

if tensor_util.is_tf_type(batch_size):
    batch_size = tensor_util.constant_value(batch_size)

if tensor_util.is_tf_type(drop_remainder):
    drop_remainder = tensor_util.constant_value(drop_remainder)

exit((batch_size, drop_remainder))
