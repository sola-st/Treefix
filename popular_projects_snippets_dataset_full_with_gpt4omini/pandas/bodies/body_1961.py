# Extracted from ./data/repos/pandas/pandas/tests/test_register_accessor.py
with ensure_removed(obj, "mine"):
    before = set(dir(obj))
    registrar("mine")(MyAccessor)
    o = obj([]) if obj is not pd.Series else obj([], dtype=object)
    assert o.mine.prop == "item"
    after = set(dir(obj))
    assert (before ^ after) == {"mine"}
    assert "mine" in obj._accessors
