# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_nonkeyword_arguments.py
assert str(inspect.signature(Foo.baz)) == "(self, bar=None, *, foobar=None)"
