# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
# GH 33963

if dtype.storage == "pyarrow":
    pytest.skip(f"not applicable for {dtype.storage}")

series = pd.Series(["a", "b", "c"], dtype=dtype)

assert 0 < series.nbytes <= series.memory_usage() < series.memory_usage(deep=True)
