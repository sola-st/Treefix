# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_readlines.py
with tm.ensure_clean("test.json") as path:
    df = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df.to_json(path, lines=True, orient="records")
    with read_json(path, lines=True, chunksize=1) as reader:
        chunked = pd.concat(reader)
    unchunked = read_json(path, lines=True)
    tm.assert_frame_equal(unchunked, chunked)
