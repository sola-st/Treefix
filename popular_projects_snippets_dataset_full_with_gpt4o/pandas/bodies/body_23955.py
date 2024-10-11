# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""create the description of the table from the axes & values"""
# provided expected rows if its passed
if expectedrows is None:
    expectedrows = max(self.nrows_expected, 10000)

d = {"name": "table", "expectedrows": expectedrows}

# description from the axes & values
d["description"] = {a.cname: a.typ for a in self.axes}

if complib:
    if complevel is None:
        complevel = self._complevel or 9
    filters = _tables().Filters(
        complevel=complevel,
        complib=complib,
        fletcher32=fletcher32 or self._fletcher32,
    )
    d["filters"] = filters
elif self._filters is not None:
    d["filters"] = self._filters

exit(d)
