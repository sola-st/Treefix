# Extracted from ./data/repos/pandas/pandas/io/stata.py

if encoding not in ("latin-1", "utf-8"):
    raise ValueError("Only latin-1 and utf-8 are supported.")
self.labname = catarray.name
self._encoding = encoding
categories = catarray.cat.categories
self.value_labels: list[tuple[float, str]] = list(
    zip(np.arange(len(categories)), categories)
)
self.value_labels.sort(key=lambda x: x[0])

self._prepare_value_labels()
