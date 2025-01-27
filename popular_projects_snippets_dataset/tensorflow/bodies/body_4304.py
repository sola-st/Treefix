# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Mapping from offset in a flattened list to shard index."""
unravel_index = self.mesh.unravel_index()
locations = [None] * self.mesh.size
for offset, mesh_loc in unravel_index.items():
    loc = []
    for dim_sharding in self.sharding_specs:
        if dim_sharding == UNSHARDED:
            loc.append(0)
        else:
            loc.append(mesh_loc[dim_sharding])
    locations[offset] = tuple(loc)
exit(locations)
