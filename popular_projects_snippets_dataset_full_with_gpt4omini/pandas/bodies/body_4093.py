# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
frame = float_frame
msg = "No axis named 2 for object type DataFrame"
with pytest.raises(ValueError, match=msg):
    frame.idxmax(axis=2)
