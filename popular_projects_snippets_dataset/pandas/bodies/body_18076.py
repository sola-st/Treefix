# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_nonkeyword_arguments.py
msg = (
    r"In a future version of pandas all arguments of Foo\.baz "
    r"except for the argument \'bar\' will be keyword-only"
)
with tm.assert_produces_warning(FutureWarning, match=msg):
    Foo().baz("qux", "quox")
