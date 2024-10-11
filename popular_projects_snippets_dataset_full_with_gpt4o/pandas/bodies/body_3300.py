# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_filter.py
fcopy = float_frame.copy()
fcopy["AA"] = 1

# regex
filtered = fcopy.filter(regex="[A]+")
assert len(filtered.columns) == 2
assert "AA" in filtered

# doesn't have to be at beginning
df = DataFrame(
    {"aBBa": [1, 2], "BBaBB": [1, 2], "aCCa": [1, 2], "aCCaBB": [1, 2]}
)

result = df.filter(regex="BB")
exp = df[[x for x in df.columns if "BB" in x]]
tm.assert_frame_equal(result, exp)
