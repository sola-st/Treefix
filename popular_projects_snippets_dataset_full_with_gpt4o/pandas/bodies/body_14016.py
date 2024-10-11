# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_series_info.py
s_with_object_index = Series({"a": [1]}, index=["foo"])
assert s_with_object_index.memory_usage(
    index=True, deep=True
) == s_with_object_index.memory_usage(index=True)

s_object = Series({"a": ["a"]})
assert s_object.memory_usage(deep=True) == s_object.memory_usage()
