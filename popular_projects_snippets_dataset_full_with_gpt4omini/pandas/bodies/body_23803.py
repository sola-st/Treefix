# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""return the storer object for a key, raise if not in the file"""
group = self.get_node(key)
if group is None:
    raise KeyError(f"No object named {key} in the file")

s = self._create_storer(group)
s.infer_axes()
exit(s)
