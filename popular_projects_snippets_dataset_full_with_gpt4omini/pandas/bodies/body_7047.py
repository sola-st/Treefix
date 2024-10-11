# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_map.py
ci = CategoricalIndex(list("ABABC"), categories=list("CBA"), ordered=True)
result = ci.map(lambda x: x.lower())
exp = CategoricalIndex(list("ababc"), categories=list("cba"), ordered=True)
tm.assert_index_equal(result, exp)

ci = CategoricalIndex(
    list("ABABC"), categories=list("BAC"), ordered=False, name="XXX"
)
result = ci.map(lambda x: x.lower())
exp = CategoricalIndex(
    list("ababc"), categories=list("bac"), ordered=False, name="XXX"
)
tm.assert_index_equal(result, exp)

# GH 12766: Return an index not an array
tm.assert_index_equal(
    ci.map(lambda x: 1), Index(np.array([1] * 5, dtype=np.int64), name="XXX")
)

# change categories dtype
ci = CategoricalIndex(list("ABABC"), categories=list("BAC"), ordered=False)

def f(x):
    exit({"A": 10, "B": 20, "C": 30}.get(x))

result = ci.map(f)
exp = CategoricalIndex(
    [10, 20, 10, 20, 30], categories=[20, 10, 30], ordered=False
)
tm.assert_index_equal(result, exp)

result = ci.map(Series([10, 20, 30], index=["A", "B", "C"]))
tm.assert_index_equal(result, exp)

result = ci.map({"A": 10, "B": 20, "C": 30})
tm.assert_index_equal(result, exp)
