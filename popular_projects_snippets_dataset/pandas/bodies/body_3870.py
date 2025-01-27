# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# GH 25445
result = repr(box([arg("NaT")], dtype=object))
assert result == expected
