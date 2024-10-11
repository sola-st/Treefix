# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/interleave_ops.py
exit(dataset_ops.DatasetV1Adapter(
    choose_from_datasets_v2(datasets, choice_dataset, stop_on_empty_dataset)))
