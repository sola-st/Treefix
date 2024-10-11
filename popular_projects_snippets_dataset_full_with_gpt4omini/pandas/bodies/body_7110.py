# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# TypeError/IndexError matches what np.insert raises in these cases

if len(index) > 0:
    err = TypeError
else:
    err = IndexError
if len(index) == 0:
    # 0 vs 0.5 in error message varies with numpy version
    msg = "index (0|0.5) is out of bounds for axis 0 with size 0"
else:
    msg = "slice indices must be integers or None or have an __index__ method"
with pytest.raises(err, match=msg):
    index.insert(0.5, "foo")

msg = "|".join(
    [
        r"index -?\d+ is out of bounds for axis 0 with size \d+",
        "loc must be an integer between",
    ]
)
with pytest.raises(IndexError, match=msg):
    index.insert(len(index) + 1, 1)

with pytest.raises(IndexError, match=msg):
    index.insert(-len(index) - 1, 1)
