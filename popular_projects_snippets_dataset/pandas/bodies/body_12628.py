# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH17200
with tm.ensure_clean("tmp_items.json") as path:
    with open(path, "w") as infile:
        infile.write('{"a": 1, "b": 2}\n{"b":2, "a" :1}\n')
    result = read_json(path, lines=True)
    expected = DataFrame([[1, 2], [1, 2]], columns=["a", "b"])
    tm.assert_frame_equal(result, expected)
