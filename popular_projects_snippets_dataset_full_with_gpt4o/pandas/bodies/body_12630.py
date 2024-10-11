# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH34473
series = Series(bigNum, dtype=object, index=["articleId"])
json = series.to_json()
expected = '{"articleId":' + str(bigNum) + "}"
assert json == expected

df = DataFrame(bigNum, dtype=object, index=["articleId"], columns=[0])
json = df.to_json()
expected = '{"0":{"articleId":' + str(bigNum) + "}}"
assert json == expected
