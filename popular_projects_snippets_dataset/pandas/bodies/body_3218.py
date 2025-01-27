# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_explode.py
# GH 39240
df = pd.DataFrame(
    {
        "A": [[0, 1, 2], np.nan, [], (3, 4)],
        "B": 1,
        "C": [["a", "b", "c"], "foo", [], ["d", "e", "f"]],
    },
    index=list("abcd"),
)
with pytest.raises(ValueError, match=error_message):
    df.explode(input_subset)
