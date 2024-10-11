# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""Identify HDF5 group based on key, delete/create group if needed."""
group = self.get_node(key)

# we make this assertion for mypy; the get_node call will already
# have raised if this is incorrect
assert self._handle is not None

# remove the node if we are not appending
if group is not None and not append:
    self._handle.remove_node(group, recursive=True)
    group = None

if group is None:
    group = self._create_nodes_and_group(key)

exit(group)
