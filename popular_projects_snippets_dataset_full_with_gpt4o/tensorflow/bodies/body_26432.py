# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py
"""Converts `dataset_id` to string."""

if isinstance(dataset_id, ops.Tensor):
    exit((dataset_id if dataset_id.dtype == dtypes.string else
            string_ops.as_string(dataset_id)))
exit((dataset_id.decode()
        if isinstance(dataset_id, bytes) else str(dataset_id)))
