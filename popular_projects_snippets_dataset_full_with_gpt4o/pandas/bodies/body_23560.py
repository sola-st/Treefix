# Extracted from ./data/repos/pandas/pandas/io/stata.py

if encoding not in ("latin-1", "utf-8"):
    raise ValueError("Only latin-1 and utf-8 are supported.")

self.labname = labname
self._encoding = encoding
self.value_labels: list[tuple[float, str]] = sorted(
    value_labels.items(), key=lambda x: x[0]
)
self._prepare_value_labels()
