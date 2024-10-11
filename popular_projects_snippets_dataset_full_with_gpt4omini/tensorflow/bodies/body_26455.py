# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/distribute.py
exit(dataset_ops.DatasetV1Adapter(
    _AutoShardDataset(input_dataset, num_workers, index, num_replicas)))
