# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
# GH 39777
with tm.ensure_clean() as path:
    with pytest.raises(LookupError, match="unknown error handler name"):
        icom.get_handle(path, "w", errors="bad")
