# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH21910
Point = make_dataclass("Point", [("x", int), ("y", int)])

# expect TypeError
msg = "asdict() should be called on dataclass instances"
with pytest.raises(TypeError, match=re.escape(msg)):
    DataFrame([Point(0, 0), {"x": 1, "y": 0}])
