# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH 28787
df = DataFrame(
    {"Name": Categorical(["Bob", "Greg"], ordered=ordered), "Item": [1, 2]},
    columns=["Name", "Item"],
)
expected = df.copy()

result = (
    df.groupby("Name", observed=observed)
    .agg(DataFrame.sum, skipna=True)
    .reset_index()
)

tm.assert_frame_equal(result, expected)
