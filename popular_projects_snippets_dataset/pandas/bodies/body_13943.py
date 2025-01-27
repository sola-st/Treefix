# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_info.py
# GH#50066
df = DataFrame(index=["a", "b"])
with tm.assert_produces_warning(None):
    result = df.memory_usage()
expected = Series(16 if IS64 else 8, index=["Index"])
tm.assert_series_equal(result, expected)
