# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py

msg = r"groupby\(\) got an unexpected keyword argument 'foo'"
with pytest.raises(TypeError, match=msg):
    roll_frame.groupby("A", foo=1)

g = roll_frame.groupby("A")
assert not g.mutated
g = get_groupby(roll_frame, by="A", mutated=True)
assert g.mutated
