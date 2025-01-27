# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_compression.py
# GH 39985 (read_json does not support user-provided binary files)
expected = pd.DataFrame({"A": [1]})

with BytesIO() as buffer:
    expected.to_json(buffer, compression=compression)
    # df = pd.read_json(buffer, compression=compression)
    # tm.assert_frame_equal(expected, df)
