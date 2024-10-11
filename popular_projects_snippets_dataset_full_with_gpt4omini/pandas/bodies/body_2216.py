# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
with tm.assert_produces_warning(warning, match="Could not infer format"):
    assert isna(to_datetime(arg, errors="coerce", format=format, cache=cache))
