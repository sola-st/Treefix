# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH#8938
# allow equality comparisons
a = Series(list("abc"), dtype="category")
b = Series(list("abc"), dtype="object")
c = Series(["a", "b", "cc"], dtype="object")
d = Series(list("acb"), dtype="object")
e = Categorical(list("abc"))
f = Categorical(list("acb"))

# vs scalar
assert not (a == "a").all()
assert ((a != "a") == ~(a == "a")).all()

assert not ("a" == a).all()
assert (a == "a")[0]
assert ("a" == a)[0]
assert not ("a" != a)[0]

# vs list-like
assert (a == a).all()
assert not (a != a).all()

assert (a == list(a)).all()
assert (a == b).all()
assert (b == a).all()
assert ((~(a == b)) == (a != b)).all()
assert ((~(b == a)) == (b != a)).all()

assert not (a == c).all()
assert not (c == a).all()
assert not (a == d).all()
assert not (d == a).all()

# vs a cat-like
assert (a == e).all()
assert (e == a).all()
assert not (a == f).all()
assert not (f == a).all()

assert (~(a == e) == (a != e)).all()
assert (~(e == a) == (e != a)).all()
assert (~(a == f) == (a != f)).all()
assert (~(f == a) == (f != a)).all()

# non-equality is not comparable
msg = "can only compare equality or not"
with pytest.raises(TypeError, match=msg):
    a < b
with pytest.raises(TypeError, match=msg):
    b < a
with pytest.raises(TypeError, match=msg):
    a > b
with pytest.raises(TypeError, match=msg):
    b > a
