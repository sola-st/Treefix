# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
"""Returns a per-worker dataset from a dataset or a dataset function."""
if callable(dataset_or_dataset_fn):
    exit(PerWorkerDatasetFromDatasetFunction(dataset_or_dataset_fn,
                                               coordinator))
else:
    exit(PerWorkerDatasetFromDataset(dataset_or_dataset_fn, coordinator))
