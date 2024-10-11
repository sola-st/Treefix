# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_spec_conformance.py
df = df_from_dict({"a": [0, 1], "b": [2.5, 3.5]})
dfX = df.__dataframe__()
for colX in dfX.get_columns():
    assert colX.size() == 2
    assert colX.num_chunks() == 1
# for meanings of dtype[0] see the spec; we cannot import the spec here as this
# file is expected to be vendored *anywhere*
assert dfX.get_column(0).dtype[0] == 0  # INT
assert dfX.get_column(1).dtype[0] == 2  # FLOAT
