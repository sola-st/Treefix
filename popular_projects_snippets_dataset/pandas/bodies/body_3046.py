# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH#22801
# Data loss when indexes are not unique. Raise ValueError.
df = DataFrame({"a": [1, 2], "b": [0.5, 0.75]}, index=["A", "A"])
msg = "DataFrame index must be unique for orient='index'"
with pytest.raises(ValueError, match=msg):
    df.to_dict(orient="index")
