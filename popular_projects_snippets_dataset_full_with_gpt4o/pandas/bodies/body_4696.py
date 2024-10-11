# Extracted from ./data/repos/pandas/pandas/tests/strings/test_cat.py
# GH 21053
box = index_or_series
values = ["a", "b"]
if other:
    other = other(values)
else:
    other = values
result = box(values, name="name").str.cat(other, sep=",")
assert result.name == "name"
