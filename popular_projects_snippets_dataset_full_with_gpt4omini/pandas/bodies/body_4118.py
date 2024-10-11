# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#21020 DataFrame.median should match Series.median
df = DataFrame({"A": Categorical([1, 2, 2, 2, 3])})
ser = df["A"]

# Double-check the Series behavior is to raise
with pytest.raises(TypeError, match="does not support reduction"):
    ser.median()

with pytest.raises(TypeError, match="does not support reduction"):
    df.median(numeric_only=False)

with pytest.raises(TypeError, match="does not support reduction"):
    df.median()

# same thing, but with an additional non-categorical column
df["B"] = df["A"].astype(int)

with pytest.raises(TypeError, match="does not support reduction"):
    df.median(numeric_only=False)

with pytest.raises(TypeError, match="does not support reduction"):
    df.median()
