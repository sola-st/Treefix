# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
index, data = tm.getMixedTypeDict()
target = DataFrame(data, index=index)

# Join on string value

source = DataFrame(
    {"MergedA": data["A"], "MergedD": data["D"]}, index=data["C"]
)
exit((target, source))
