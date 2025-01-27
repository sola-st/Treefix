# Extracted from ./data/repos/pandas/pandas/core/arrays/string_arrow.py
if pa_version_under6p0:
    msg = "pyarrow>=6.0.0 is required for PyArrow backed ArrowExtensionArray."
    raise ImportError(msg)
