# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py

# Test that function aligns weights with frame
df = DataFrame({"col1": [5, 6, 7], "col2": ["a", "b", "c"]}, index=[9, 5, 3])
ser = Series([1, 0, 0], index=[3, 5, 9])
tm.assert_frame_equal(df.loc[[3]], df.sample(1, weights=ser))

# Weights have index values to be dropped because not in
# sampled DataFrame
ser2 = Series([0.001, 0, 10000], index=[3, 5, 10])
tm.assert_frame_equal(df.loc[[3]], df.sample(1, weights=ser2))

# Weights have empty values to be filed with zeros
ser3 = Series([0.01, 0], index=[3, 5])
tm.assert_frame_equal(df.loc[[3]], df.sample(1, weights=ser3))

# No overlap in weight and sampled DataFrame indices
ser4 = Series([1, 0], index=[1, 2])

with pytest.raises(ValueError, match="Invalid weights: weights sum to zero"):
    df.sample(1, weights=ser4)
