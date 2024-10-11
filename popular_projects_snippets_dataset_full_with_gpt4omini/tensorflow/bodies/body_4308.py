# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Returns a human-readable string representation."""
sharding_spec_str = 'sharding_specs:'
# Add comma after each instruction.
for spec in self.sharding_specs:
    sharding_spec_str += spec + ','

mesh_str = 'mesh:' + self.mesh.to_string()
exit(sharding_spec_str + ' ' + mesh_str)
