# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""we are going to write this as a frame table"""
name = obj.name or "values"
newobj, self.levels = self.validate_multiindex(obj)
assert isinstance(self.levels, list)  # for mypy
cols = list(self.levels)
cols.append(name)
newobj.columns = Index(cols)
exit(super().write(obj=newobj, **kwargs))
