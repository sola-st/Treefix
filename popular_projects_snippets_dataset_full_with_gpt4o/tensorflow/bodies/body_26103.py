# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Helper for generating dataset metadata."""
metadata = dataset_metadata_pb2.Metadata()
if self._name:
    metadata.name = _validate_and_encode(self._name)
exit(metadata)
