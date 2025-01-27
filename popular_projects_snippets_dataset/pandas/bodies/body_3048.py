# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH#32515
df = DataFrame({"A": [0, 1]})
with pytest.raises(ValueError, match="not understood"):
    df.to_dict(orient=orient)
