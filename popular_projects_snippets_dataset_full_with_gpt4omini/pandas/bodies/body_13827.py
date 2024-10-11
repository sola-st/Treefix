# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 14194
# setup dataframe with multiple column levels and indices
i1 = MultiIndex.from_arrays(
    [["a", "a"], [0, 1]], names=["idx_level_0", "idx_level_1"]
)
i2 = MultiIndex.from_arrays(
    [["b", "b"], [0, 1]], names=["col_level_0", "col_level_1"]
)
df = DataFrame([[1, 2], [3, 4]], index=i1, columns=i2)
ctx = df.style._translate(True, True)
# column headers
assert ctx["head"][0][2]["is_visible"]
assert ctx["head"][1][2]["is_visible"]
assert ctx["head"][1][3]["display_value"] == "1"
# indices
assert ctx["body"][0][0]["is_visible"]
# data
assert ctx["body"][1][2]["is_visible"]
assert ctx["body"][1][2]["display_value"] == "3"
assert ctx["body"][1][3]["is_visible"]
assert ctx["body"][1][3]["display_value"] == "4"

# hide top column level, which hides both columns
ctx = df.style.hide("b", axis="columns")._translate(True, True)
assert not ctx["head"][0][2]["is_visible"]  # b
assert not ctx["head"][1][2]["is_visible"]  # 0
assert not ctx["body"][1][2]["is_visible"]  # 3
assert ctx["body"][0][0]["is_visible"]  # index

# hide first column only
ctx = df.style.hide([("b", 0)], axis="columns")._translate(True, True)
assert not ctx["head"][0][2]["is_visible"]  # b
assert ctx["head"][0][3]["is_visible"]  # b
assert not ctx["head"][1][2]["is_visible"]  # 0
assert not ctx["body"][1][2]["is_visible"]  # 3
assert ctx["body"][1][3]["is_visible"]
assert ctx["body"][1][3]["display_value"] == "4"

# hide second column and index
ctx = df.style.hide([("b", 1)], axis=1).hide(axis=0)._translate(True, True)
assert not ctx["body"][0][0]["is_visible"]  # index
assert len(ctx["head"][0]) == 3
assert ctx["head"][0][1]["is_visible"]  # b
assert ctx["head"][1][1]["is_visible"]  # 0
assert not ctx["head"][1][2]["is_visible"]  # 1
assert not ctx["body"][1][3]["is_visible"]  # 4
assert ctx["body"][1][2]["is_visible"]
assert ctx["body"][1][2]["display_value"] == "3"

# hide top row level, which hides both rows so body empty
ctx = df.style.hide("a", axis="index")._translate(True, True)
assert ctx["body"] == []

# hide first row only
ctx = df.style.hide(("a", 0), axis="index")._translate(True, True)
for i in [0, 1, 2, 3]:
    assert "row1" in ctx["body"][0][i]["class"]  # row0 not included in body
    assert ctx["body"][0][i]["is_visible"]
