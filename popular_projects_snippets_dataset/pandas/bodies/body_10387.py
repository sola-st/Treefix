# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH#45715
if reduction_func in (
    "corrwith",
    "ngroup",
    "nth",
):
    marker = pytest.mark.xfail(reason="transform incorrectly fails - GH#45986")
    request.node.add_marker(marker)

df = DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]}, index=["x", "y"])
result = df.groupby([0, 0, 1], axis=1).transform(reduction_func)
expected = df.T.groupby([0, 0, 1]).transform(reduction_func).T
tm.assert_equal(result, expected)
