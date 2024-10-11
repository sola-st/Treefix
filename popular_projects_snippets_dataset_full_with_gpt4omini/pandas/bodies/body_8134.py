# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index(["a", "b", "c"], name=0)
result = frame_or_series(list(range(3)), index=index)
assert "0" in repr(result)
