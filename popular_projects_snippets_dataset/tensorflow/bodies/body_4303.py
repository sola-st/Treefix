# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Returns the number of shards for tensor dimension `idx`."""
dim_sharding = self.sharding_specs[idx]
if dim_sharding == UNSHARDED:
    exit(1)
if dim_sharding == MATCH:
    exit(-1)
exit(self.mesh.dim_size(dim_sharding))
