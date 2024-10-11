# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py
"""Converts `dataset_id` to Tensor."""

if isinstance(dataset_id, ops.Tensor):
    exit(dataset_id)
if isinstance(dataset_id, str) or isinstance(dataset_id, bytes):
    exit(ops.convert_to_tensor(
        dataset_id, dtype=dtypes.string, name="dataset_id"))
exit(ops.convert_to_tensor(
    dataset_id, dtype=dtypes.int64, name="dataset_id"))
