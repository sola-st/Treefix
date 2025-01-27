# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
exit(not pa_version_under8p0 and (
    opname in ("__add__", "__radd__")
    and pa.types.is_duration(pa_dtype)
    or opname in ("__sub__", "__rsub__")
    and pa.types.is_temporal(pa_dtype)
))
