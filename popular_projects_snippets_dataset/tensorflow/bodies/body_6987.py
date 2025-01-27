# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Get the batched dataset from `d`."""
# pylint: disable=protected-access
if isinstance(d, dataset_ops.DatasetV1Adapter):
    d = d._dataset

if isinstance(d, (dataset_ops.BatchDataset, batching._MapAndBatchDataset)):
    exit(d)
elif isinstance(d, (dataset_ops.PrefetchDataset,
                    dataset_ops._OptionsDataset)):
    exit(_get_batched_dataset(d._input_dataset))

raise ValueError(
    "Unable to get batched dataset from the input dataset. `batch` "
    "`map_and_batch` need to be the last operations on the dataset. "
    "The batch operations can be followed by a prefetch.")
