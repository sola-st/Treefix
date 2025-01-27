# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
# A classic namedtuple and an equivalent cppy.
Foo1 = collections.namedtuple("Foo", ["a", "b"])
Foo2 = collections.namedtuple("Foo", ["a", "b"])
self.assertTrue(nest.same_namedtuples(Foo1(1, 2), Foo1(3, 4)))
self.assertTrue(nest.same_namedtuples(Foo1(1, 2), Foo2(3, 4)))

# Non-equivalent namedtuples.
Bar = collections.namedtuple("Bar", ["a", "b"])
self.assertFalse(nest.same_namedtuples(Foo1(1, 2), Bar(1, 2)))
FooXY = collections.namedtuple("Foo", ["x", "y"])
self.assertFalse(nest.same_namedtuples(Foo1(1, 2), FooXY(1, 2)))

# An equivalent subclass from the typing module
class Foo(NamedTuple):
    a: int
    b: int
self.assertTrue(nest.same_namedtuples(Foo1(1, 2), Foo(3, 4)))
