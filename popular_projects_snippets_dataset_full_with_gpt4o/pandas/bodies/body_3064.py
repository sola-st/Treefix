# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH#50795
df = DataFrame({"a": [1, NA]}, dtype="Int64")
result = df.to_dict(orient=orient)
assert result == expected
