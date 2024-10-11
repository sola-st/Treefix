# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py

# GH 14848 - regression from 0.19.0 to 0.19.1
df1 = DataFrame(
    {
        "x": [1, 2, 3, 4, 5] * 3,
        "y": [10, 20, 30, 40, 50] * 3,
        "z": [100, 200, 300, 400, 500] * 3,
    }
)
df1["k"] = [(0, 0, 1), (0, 1, 0), (1, 0, 0)] * 5
df2 = df1.rename(columns={"k": "key"})
msg = "Names should be list-like for a MultiIndex"
with pytest.raises(ValueError, match=msg):
    df1.groupby("k").describe()
with pytest.raises(ValueError, match=msg):
    df2.groupby("key").describe()
