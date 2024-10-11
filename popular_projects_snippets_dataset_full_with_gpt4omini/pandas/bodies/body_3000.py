# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
df = DataFrame(
    {
        "c": Categorical(
            ["A", np.nan, "B", np.nan, "C"],
            categories=["A", "B", "C"],
            ordered=True,
        )
    }
)

with pytest.raises(ValueError, match="invalid na_position: bad_position"):
    df.sort_values(by="c", ascending=False, na_position="bad_position")
