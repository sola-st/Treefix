# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH 1134
# GH 50083 to clarify that index and columns must be identically labeled
if frame_or_series is not Series:
    msg = (
        rf"Can only compare identically-labeled \(both index and columns\) "
        f"{frame_or_series.__name__} objects"
    )
    left = left.to_frame()
    right = right.to_frame()
else:
    msg = (
        f"Can only compare identically-labeled {frame_or_series.__name__} "
        f"objects"
    )

with pytest.raises(ValueError, match=msg):
    left == right
with pytest.raises(ValueError, match=msg):
    right == left

with pytest.raises(ValueError, match=msg):
    left != right
with pytest.raises(ValueError, match=msg):
    right != left

with pytest.raises(ValueError, match=msg):
    left < right
with pytest.raises(ValueError, match=msg):
    right < left
