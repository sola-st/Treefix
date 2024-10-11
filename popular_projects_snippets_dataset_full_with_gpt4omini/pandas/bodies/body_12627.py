# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH17200

result = read_json(
    "s3n://pandas-test/items.jsonl", lines=True, storage_options=s3so
)
expected = DataFrame([[1, 2], [1, 2]], columns=["a", "b"])
tm.assert_frame_equal(result, expected)
