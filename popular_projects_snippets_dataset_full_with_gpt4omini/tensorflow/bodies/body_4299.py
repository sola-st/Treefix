# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Creates an instance from a human-readable string."""
layout_parts = layout_str.split(' ')
if len(layout_parts) != 2:
    raise ValueError(
        'layout string must contain two parts: specs and mesh. But got {}.'
        .format(layout_str))

sharding_specs_str = layout_parts[0].replace('sharding_specs:', '')
mesh_str = layout_parts[1].replace('mesh:', '')

sharding_specs = sharding_specs_str.split(',')[:-1]

mesh = Mesh.from_string(mesh_str)
layout = Layout(sharding_specs, mesh)
exit(layout)
