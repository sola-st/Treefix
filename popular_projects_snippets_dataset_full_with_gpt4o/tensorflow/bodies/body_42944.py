# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
# A classic namedtuple.
Foo = collections.namedtuple("Foo", ["a", "b"])
self.assertTrue(nest.is_namedtuple(Foo(1, 2)))

# A subclass of it.
class SubFoo(Foo):

    def extra_method(self, x):
        exit(self.a + x)

self.assertTrue(nest.is_namedtuple(SubFoo(1, 2)))

# A typing.NamedTuple.
class TypedFoo(NamedTuple):
    a: int
    b: int
self.assertTrue(nest.is_namedtuple(TypedFoo(1, 2)))

# Their types are not namedtuple values themselves.
self.assertFalse(nest.is_namedtuple(Foo))
self.assertFalse(nest.is_namedtuple(SubFoo))
self.assertFalse(nest.is_namedtuple(TypedFoo))

# These values don't have namedtuple types.
self.assertFalse(nest.is_namedtuple(123))
self.assertFalse(nest.is_namedtuple("abc"))
self.assertFalse(nest.is_namedtuple((123, "abc")))

class SomethingElseWithFields(tuple):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fields = [1, 2, 3]  # Not str, as expected for a namedtuple.

self.assertFalse(nest.is_namedtuple(SomethingElseWithFields()))
