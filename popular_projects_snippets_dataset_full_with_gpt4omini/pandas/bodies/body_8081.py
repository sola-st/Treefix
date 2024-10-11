# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 18304
index = Index(values)
expected = Index(["b"])

result = index.drop(to_drop)
tm.assert_index_equal(result, expected)

removed = index.drop(to_drop[0])
for drop_me in to_drop[1], [to_drop[1]]:
    result = removed.drop(drop_me)
    tm.assert_index_equal(result, expected)

removed = index.drop(to_drop[1])
msg = rf"\"\[{re.escape(to_drop[1].__repr__())}\] not found in axis\""
for drop_me in to_drop[1], [to_drop[1]]:
    with pytest.raises(KeyError, match=msg):
        removed.drop(drop_me)
