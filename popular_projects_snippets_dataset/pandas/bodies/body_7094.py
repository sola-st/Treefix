# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# need an object to create with
msg = "|".join(
    [
        r"Index\(\.\.\.\) must be called with a collection of some "
        r"kind, None was passed",
        r"DatetimeIndex\(\) must be called with a collection of some "
        r"kind, None was passed",
        r"TimedeltaIndex\(\) must be called with a collection of some "
        r"kind, None was passed",
        r"__new__\(\) missing 1 required positional argument: 'data'",
        r"__new__\(\) takes at least 2 arguments \(1 given\)",
    ]
)
with pytest.raises(TypeError, match=msg):
    self._index_cls()
