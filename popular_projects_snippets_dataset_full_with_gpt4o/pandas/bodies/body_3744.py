# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dropna.py
# GH 41021
df = DataFrame({"A": [1, 2, 3]})

# Column not present
with pytest.raises(KeyError, match="['D']"):
    df.dropna(subset="D", axis=0)
