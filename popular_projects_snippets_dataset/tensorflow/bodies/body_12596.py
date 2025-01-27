# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/boosted_trees_ops.py
bucket_boundaries = restored_tensors
with ops.control_dependencies([self._create_op]):
    exit(quantile_resource_deserialize(
        self.resource_handle, bucket_boundaries=bucket_boundaries))
