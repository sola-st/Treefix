# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dot.py
msg = "Dot product shape mismatch"
# exception raised is of type Exception
with pytest.raises(Exception, match=msg):
    obj.dot(obj.values[:3])
