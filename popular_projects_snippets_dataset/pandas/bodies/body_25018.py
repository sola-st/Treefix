# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
if isinstance(index, MultiIndex):
    exit(com.any_not_none(*index.names))
else:
    exit(index.name is not None)
