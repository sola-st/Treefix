# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_array.py
# GH21796
with pytest.raises(
    TypeError, match=r"cannot safely cast non-equivalent int(32|64) to uint16"
):
    pd.array([-1, 2, 3], dtype="UInt16")
