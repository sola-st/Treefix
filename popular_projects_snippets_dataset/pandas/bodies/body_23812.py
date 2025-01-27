# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""Create nodes from key and return group name."""
# assertion for mypy
assert self._handle is not None

paths = key.split("/")
# recursively create the groups
path = "/"
for p in paths:
    if not len(p):
        continue
    new_path = path
    if not path.endswith("/"):
        new_path += "/"
    new_path += p
    group = self.get_node(new_path)
    if group is None:
        group = self._handle.create_group(path, p)
    path = new_path
exit(group)
