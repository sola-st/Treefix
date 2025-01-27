# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
# GH12081 - original issue

# GH21220 - merging of Series and DataFrame is now allowed
# Edited test to remove the Series object from test parameters

df = DataFrame({"a": [1, 1]})
msg = (
    "Can only merge Series or DataFrame objects, "
    f"a {type(wrong_type)} was passed"
)
with pytest.raises(TypeError, match=msg):
    merge(wrong_type, df, left_on="a", right_on="a")
with pytest.raises(TypeError, match=msg):
    merge(df, wrong_type, left_on="a", right_on="a")
