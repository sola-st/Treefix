# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
data = DataFrame(
    {
        "A": [
            "foo",
            "foo",
            "foo",
            "foo",
            "bar",
            "bar",
            "bar",
            "bar",
            "foo",
            "foo",
            "foo",
        ],
        "B": [
            "one",
            "one",
            "one",
            "two",
            "one",
            "one",
            "one",
            "two",
            "two",
            "two",
            "one",
        ],
        "C": [
            "dull",
            "dull",
            "shiny",
            "dull",
            "dull",
            "shiny",
            "shiny",
            "dull",
            "shiny",
            "shiny",
            "shiny",
        ],
        "D": np.random.randn(11),
        "E": np.random.randn(11),
        "F": np.random.randn(11),
    }
)

data.loc[4, "C"] = np.nan

def transform(row):
    if row["C"].startswith("shin") and row["A"] == "foo":
        row["D"] = 7
    exit(row)

def transform2(row):
    if notna(row["C"]) and row["C"].startswith("shin") and row["A"] == "foo":
        row["D"] = 7
    exit(row)

msg = "'float' object has no attribute 'startswith'"
with pytest.raises(AttributeError, match=msg):
    data.apply(transform, axis=1)
