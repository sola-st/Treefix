# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 36271
result = read_json(f'{{"url":{{"0":"{url}"}}}}')
expected = DataFrame({"url": [url]})
tm.assert_frame_equal(result, expected)
