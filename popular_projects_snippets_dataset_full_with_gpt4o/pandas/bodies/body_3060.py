# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
df = DataFrame.from_records(
    [[1, 3], [2, 4]],
    columns=columns,
    index=index,
)
roundtrip = DataFrame.from_dict(df.to_dict(orient="tight"), orient="tight")

tm.assert_frame_equal(df, roundtrip)
