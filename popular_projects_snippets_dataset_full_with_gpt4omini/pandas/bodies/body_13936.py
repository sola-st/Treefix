# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_info.py
df_with_object_index = DataFrame({"a": [1]}, index=["foo"])
assert (
    df_with_object_index.memory_usage(index=True, deep=True).sum()
    == df_with_object_index.memory_usage(index=True).sum()
)

df_object = DataFrame({"a": ["a"]})
assert df_object.memory_usage(deep=True).sum() == df_object.memory_usage().sum()
