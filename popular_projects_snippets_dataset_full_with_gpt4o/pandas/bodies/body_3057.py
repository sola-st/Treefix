# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH22620 & GH21256

df = DataFrame({"a": data})
d = df.to_dict(orient="records")
assert all(type(record["a"]) is dtype for record in d)
