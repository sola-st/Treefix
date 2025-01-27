# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 14194
df = DataFrame(
    {"A": [1, 2], "B": [1, 2]},
    index=MultiIndex.from_arrays(
        [["a", "a"], [0, 1]], names=["idx_level_0", "idx_level_1"]
    ),
)
ctx1 = df.style._translate(True, True)
# tests for 'a' and '0'
assert ctx1["body"][0][0]["is_visible"]
assert ctx1["body"][0][1]["is_visible"]
# check for blank header rows
assert len(ctx1["head"][0]) == 4  # two visible indexes and two data columns

ctx2 = df.style.hide(axis="index")._translate(True, True)
# tests for 'a' and '0'
assert not ctx2["body"][0][0]["is_visible"]
assert not ctx2["body"][0][1]["is_visible"]
# check for blank header rows
assert len(ctx2["head"][0]) == 3  # one hidden (col name) and two data columns
assert not ctx2["head"][0][0]["is_visible"]
