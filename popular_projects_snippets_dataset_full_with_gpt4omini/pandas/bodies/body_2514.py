# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_get_value.py
# partial w/ MultiIndex raise exception
index = MultiIndex.from_tuples([(0, 1), (0, 2), (1, 1), (1, 2)])
df = DataFrame(index=index, columns=range(4))
with pytest.raises(KeyError, match=r"^0$"):
    df._get_value(0, 1)
