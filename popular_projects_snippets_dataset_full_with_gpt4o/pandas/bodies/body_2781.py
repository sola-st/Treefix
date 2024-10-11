# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# GH#2419
# additional specific object based tests

# A few dataframe test with degenerate weights.
easy_weight_list = [0] * 10
easy_weight_list[5] = 1

df = DataFrame(
    {
        "col1": range(10, 20),
        "col2": range(20, 30),
        "colString": ["a"] * 10,
        "easyweights": easy_weight_list,
    }
)
sample1 = df.sample(n=1, weights="easyweights")
tm.assert_frame_equal(sample1, df.iloc[5:6])

# Ensure proper error if string given as weight for Series or
# DataFrame with axis = 1.
ser = Series(range(10))
msg = "Strings cannot be passed as weights when sampling from a Series."
with pytest.raises(ValueError, match=msg):
    ser.sample(n=3, weights="weight_column")

msg = (
    "Strings can only be passed to weights when sampling from rows on a "
    "DataFrame"
)
with pytest.raises(ValueError, match=msg):
    df.sample(n=1, weights="weight_column", axis=1)

# Check weighting key error
with pytest.raises(
    KeyError, match="'String passed to weights not a valid column'"
):
    df.sample(n=3, weights="not_a_real_column_name")

# Check that re-normalizes weights that don't sum to one.
weights_less_than_1 = [0] * 10
weights_less_than_1[0] = 0.5
tm.assert_frame_equal(df.sample(n=1, weights=weights_less_than_1), df.iloc[:1])

###
# Test axis argument
###

# Test axis argument
df = DataFrame({"col1": range(10), "col2": ["a"] * 10})
second_column_weight = [0, 1]
tm.assert_frame_equal(
    df.sample(n=1, axis=1, weights=second_column_weight), df[["col2"]]
)

# Different axis arg types
tm.assert_frame_equal(
    df.sample(n=1, axis="columns", weights=second_column_weight), df[["col2"]]
)

weight = [0] * 10
weight[5] = 0.5
tm.assert_frame_equal(df.sample(n=1, axis="rows", weights=weight), df.iloc[5:6])
tm.assert_frame_equal(
    df.sample(n=1, axis="index", weights=weight), df.iloc[5:6]
)

# Check out of range axis values
msg = "No axis named 2 for object type DataFrame"
with pytest.raises(ValueError, match=msg):
    df.sample(n=1, axis=2)

msg = "No axis named not_a_name for object type DataFrame"
with pytest.raises(ValueError, match=msg):
    df.sample(n=1, axis="not_a_name")

ser = Series(range(10))
with pytest.raises(ValueError, match="No axis named 1 for object type Series"):
    ser.sample(n=1, axis=1)

# Test weight length compared to correct axis
msg = "Weights and axis to be sampled must be of same length"
with pytest.raises(ValueError, match=msg):
    df.sample(n=1, axis=1, weights=[0.5] * 10)
