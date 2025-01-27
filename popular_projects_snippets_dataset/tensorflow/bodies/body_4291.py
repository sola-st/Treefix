# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Builds a Layout from a list of dimension names and a Mesh.

    Args:
      sharding_specs: List of sharding specifications, each corresponding to a
        tensor axis. Each specification (dim_sharding) can either be a mesh
        dimension or the special value UNSHARDED.
      mesh: A mesh configuration for the Tensor.

    Returns:
      A valid Layout built with given layout & mesh.
    """
# Validate mesh
if not isinstance(mesh, Mesh):
    raise ValueError('mesh is not a valid Mesh object.')

# Validate sharding spec
for _, dim_sharding in enumerate(sharding_specs):
    # If special value no need to check for uniqueness, just skip.
    if dim_sharding == UNSHARDED or dim_sharding == MATCH:
        continue
    # Check dim_sharding is unique.
    if sharding_specs.count(dim_sharding) > 1:
        raise ValueError(
            ('Mesh dimension {mesh_dim} was repeated in sharding ' +
             'specification {sharding_specs}. Mesh dimensions must be unique ' +
             'in a layout.').format(
                 mesh_dim=dim_sharding, sharding_specs=sharding_specs))
    # Check dim_sharding is mesh dimension.
    if dim_sharding not in mesh:
        raise ValueError(
            ('{dim_sharding}: A dimension sharding must either be a ' +
             'valid mesh dimension or UNSHARDED.').format(
                 dim_sharding=dim_sharding))

    # Set object's state
self.sharding_specs = sharding_specs
self.rank = len(sharding_specs)
self.mesh = mesh
self.shape = [self.num_shards(i) for i in range(self.rank)]
