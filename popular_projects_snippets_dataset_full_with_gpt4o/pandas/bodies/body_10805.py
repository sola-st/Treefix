# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH-9614
# test fix for when group by on None resulted in
# coercion of dtype categorical -> float
df = DataFrame({"A": [None] * 3, "B": Categorical(["train", "train", "test"])})
result = df.groupby("A").first()["B"]
expected = Series(
    Categorical([], categories=["test", "train"]),
    index=Series([], dtype="object", name="A"),
    name="B",
)
tm.assert_series_equal(result, expected)
