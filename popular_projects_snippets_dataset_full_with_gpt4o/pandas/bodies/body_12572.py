# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
df = DataFrame(columns=["jim", "joe"])
assert not df._is_mixed_type
tm.assert_frame_equal(
    read_json(df.to_json(), dtype=dict(df.dtypes)), df, check_index_type=False
)
# GH 7445
result = DataFrame({"test": []}, index=[]).to_json(orient="columns")
expected = '{"test":{}}'
assert result == expected
