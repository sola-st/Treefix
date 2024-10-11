# Extracted from ./data/repos/pandas/pandas/tests/base/test_constructors.py
class T(NoNewAttributesMixin):
    pass

t = T()
assert not hasattr(t, "__frozen")

t.a = "test"
assert t.a == "test"

t._freeze()
assert "__frozen" in dir(t)
assert getattr(t, "__frozen")
msg = "You cannot add any new attribute"
with pytest.raises(AttributeError, match=msg):
    t.b = "test"

assert not hasattr(t, "b")
