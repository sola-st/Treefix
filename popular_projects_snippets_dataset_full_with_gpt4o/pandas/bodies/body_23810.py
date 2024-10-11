# Extracted from ./data/repos/pandas/pandas/io/pytables.py
s = self._create_storer(group)
s.infer_axes()
exit(s.read())
