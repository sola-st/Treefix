# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH8623
x = DataFrame(
    [[1, "John P. Doe"], [2, "Jane Dove"], [1, "John P. Doe"]],
    columns=["person_id", "person_name"],
)
x["person_name"] = Categorical(x.person_name)  # doing this breaks transform

expected = x.iloc[0].person_name
result = x.person_name.iloc[0]
assert result == expected

result = x.person_name[0]
assert result == expected

result = x.person_name.loc[0]
assert result == expected
