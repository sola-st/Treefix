# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_delitem.py
f = float_frame.copy()
del f["D"]
assert len(f.columns) == 3
with pytest.raises(KeyError, match=r"^'D'$"):
    del f["D"]
del f["B"]
assert len(f.columns) == 2
