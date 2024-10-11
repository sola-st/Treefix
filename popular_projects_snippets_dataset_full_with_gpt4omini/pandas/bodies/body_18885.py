# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
data = makeStringIndex(_N)
data = Index(data, dtype=object)
index = makeStringIndex(_N)
exit(Series(data, index=index, name=name))
