# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# GH#47986
df = DataFrame(
    {"a": [1, 2]},
    index=MultiIndex.from_arrays([Series([NA, 1], dtype="Int64")]),
)

result = df.to_string()
expected = """      a
<NA>  1
1     2"""
assert result == expected
