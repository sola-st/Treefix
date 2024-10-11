# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
# GH 8860
df = DataFrame(
    {
        "MAKE": ["Honda", "Acura", "Tesla", "Honda", "Honda", "Acura"],
        "MODEL": ["Sedan", "Sedan", "Electric", "Pickup", "Sedan", "Sedan"],
    }
)
categories = ["Sedan", "Electric", "Pickup"]
df["MODEL"] = df["MODEL"].astype("category").cat.set_categories(categories)
result = crosstab(df["MAKE"], df["MODEL"])

expected_index = Index(["Acura", "Honda", "Tesla"], name="MAKE")
expected_columns = CategoricalIndex(
    categories, categories=categories, ordered=False, name="MODEL"
)
expected_data = [[2, 0, 0], [2, 0, 1], [0, 1, 0]]
expected = DataFrame(
    expected_data, index=expected_index, columns=expected_columns
)
tm.assert_frame_equal(result, expected)
