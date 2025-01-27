# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH 26988
df = DataFrame([[1, 1], [2, 2]], columns=["a", "b"], dtype="category")

final_data = np.array(final_data)

a = pd.Categorical(final_data[:, 0], categories=[3, 2])

ex_cat = [3, 2] if replace_dict["b"] == 1 else [1, 3]
b = pd.Categorical(final_data[:, 1], categories=ex_cat)

expected = DataFrame({"a": a, "b": b})
result = df.replace(replace_dict, 3)
tm.assert_frame_equal(result, expected)
msg = (
    r"Attributes of DataFrame.iloc\[:, 0\] \(column name=\"a\"\) are "
    "different"
)
with pytest.raises(AssertionError, match=msg):
    # ensure non-inplace call does not affect original
    tm.assert_frame_equal(df, expected)
return_value = df.replace(replace_dict, 3, inplace=True)
assert return_value is None
tm.assert_frame_equal(df, expected)
