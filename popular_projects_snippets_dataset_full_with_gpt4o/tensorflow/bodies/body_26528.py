# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/interleave_ops.py
exit(dataset_ops.DatasetV1Adapter(
    sample_from_datasets_v2(datasets, weights, seed, stop_on_empty_dataset)))
