# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Returns the layout with the give dimensions deleted."""
if not isinstance(dims, list):
    dims = [dims]
new_specs = [
    spec for i, spec in enumerate(self.sharding_specs) if i not in dims
]
exit(Layout(new_specs, self.mesh))
