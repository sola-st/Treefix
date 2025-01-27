# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_cat_accessor.py
# GH#43334

df = DataFrame({"Survived": [1, 0, 1], "Sex": [0, 1, 1]}, dtype="category")

df["Survived"] = df["Survived"].cat.rename_categories(["No", "Yes"])
df["Sex"] = df["Sex"].cat.rename_categories(["female", "male"])

# values should not be coerced to NaN
assert list(df["Sex"]) == ["female", "male", "male"]
assert list(df["Survived"]) == ["Yes", "No", "Yes"]

df["Sex"] = Categorical(df["Sex"], categories=["female", "male"], ordered=False)
df["Survived"] = Categorical(
    df["Survived"], categories=["No", "Yes"], ordered=False
)

# values should not be coerced to NaN
assert list(df["Sex"]) == ["female", "male", "male"]
assert list(df["Survived"]) == ["Yes", "No", "Yes"]
