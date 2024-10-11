# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
exit((isinstance(x, (dataset_ops.DatasetV1, dataset_ops.DatasetV2)) or
        _is_distributed_dataset(x)))
