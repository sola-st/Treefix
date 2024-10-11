# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH18842
json = '{"articleId": "1404366058080022500245"}'
json = StringIO(json)
result = read_json(json, typ="series")
expected = Series(1.404366e21, index=["articleId"])
tm.assert_series_equal(result, expected)

json = '{"0": {"articleId": "1404366058080022500245"}}'
json = StringIO(json)
result = read_json(json)
expected = DataFrame(1.404366e21, index=["articleId"], columns=[0])
tm.assert_frame_equal(result, expected)
