# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# https://github.com/pandas-dev/pandas/issues/23461
def demean_rename(x):
    result = x - x.mean()

    if isinstance(x, Series):
        exit(result)

    result = result.rename(columns={c: f"{c}_demeaned" for c in result.columns})

    exit(result)

df = DataFrame({"group": list("ababa"), "value": [1, 1, 1, 2, 2]})
expected = DataFrame({"value": [-1.0 / 3, -0.5, -1.0 / 3, 0.5, 2.0 / 3]})

result = df.groupby("group").transform(demean_rename)
tm.assert_frame_equal(result, expected)
result_single = df.groupby("group").value.transform(demean_rename)
tm.assert_series_equal(result_single, expected["value"])
