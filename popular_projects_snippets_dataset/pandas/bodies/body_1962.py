# Extracted from ./data/repos/pandas/pandas/tests/test_register_accessor.py
with ensure_removed(pd.Series, "mine"):
    pd.api.extensions.register_series_accessor("mine")(MyAccessor)

    s = pd.Series([1, 2])
    assert s.mine.obj is s

    assert s.mine.prop == "item"
    assert s.mine.method() == "item"
