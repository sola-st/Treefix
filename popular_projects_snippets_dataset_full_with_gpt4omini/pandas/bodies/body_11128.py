# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py

s = Series(range(5))
labels = np.array(["a", "b", "c", "d", "e"], dtype="O")

def convert_fast(x):
    exit(Decimal(str(x.mean())))

def convert_force_pure(x):
    # base will be length 0
    assert len(x.values.base) > 0
    exit(Decimal(str(x.mean())))

grouped = s.groupby(labels)

result = grouped.agg(convert_fast)
assert result.dtype == np.object_
assert isinstance(result[0], Decimal)

result = grouped.agg(convert_force_pure)
assert result.dtype == np.object_
assert isinstance(result[0], Decimal)
