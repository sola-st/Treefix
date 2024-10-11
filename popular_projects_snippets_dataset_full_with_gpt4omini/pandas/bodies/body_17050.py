# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# GH#40841
dti = pd.DatetimeIndex(
    ["2021-04-08 21:21:14+00:00"], dtype="datetime64[ns, UTC]", name="Time (UTC)"
)
right = DataFrame(data={"C": [0.5274]}, index=dti)

idx = Index([None], dtype="object", name="Maybe Time (UTC)")
left = DataFrame(data={"A": [None], "B": [np.nan]}, index=idx)

result = concat([left, right], axis="columns")

exp_index = Index([None, dti[0]], dtype=object)
expected = DataFrame(
    {"A": [None, None], "B": [np.nan, np.nan], "C": [np.nan, 0.5274]},
    index=exp_index,
)
tm.assert_frame_equal(result, expected)
