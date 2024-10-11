# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
# GH9748
msg = (
    "cannot do slice indexing on CategoricalIndex with these "
    r"indexers \[1\] of type int"
)
with pytest.raises(TypeError, match=msg):
    df.loc[1:5]

result = df.loc["b":"c"]
expected = df.iloc[[2, 3, 4]]
tm.assert_frame_equal(result, expected)
