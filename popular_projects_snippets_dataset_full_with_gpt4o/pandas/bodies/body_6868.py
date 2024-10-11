# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
# GH 21115
# MultiIndex is tested separately in test_multi.py
index = index_flat

assert index.droplevel([]).equals(index)

for level in [index.name, [index.name]]:
    if isinstance(index.name, tuple) and level is index.name:
        # GH 21121 : droplevel with tuple name
        continue
    msg = (
        "Cannot remove 1 levels from an index with 1 levels: at least one "
        "level must be left."
    )
    with pytest.raises(ValueError, match=msg):
        index.droplevel(level)

for level in "wrong", ["wrong"]:
    with pytest.raises(
        KeyError,
        match=r"'Requested level \(wrong\) does not match index name \(None\)'",
    ):
        index.droplevel(level)
