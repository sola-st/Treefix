# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH22620 & GH21256

df = DataFrame({"a": data}, index=[0])
d = df.to_dict(orient="records")
result = type(d[0]["a"])
assert result is expected_dtype
