# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH 17605
if reduction_func == "ngroup":
    pytest.skip("ngroup is not truly a reduction")

if reduction_func == "corrwith":  # GH 32293
    mark = pytest.mark.xfail(
        reason="TODO: implemented SeriesGroupBy.corrwith. See GH 32293"
    )
    request.node.add_marker(mark)

df = DataFrame(
    {
        "cat_1": Categorical(list("AABB"), categories=list("ABCD")),
        "cat_2": Categorical(list("AB") * 2, categories=list("ABCD")),
        "value": [0.1] * 4,
    }
)
args = get_groupby_method_args(reduction_func, df)

expected_length = 4 if observed else 16

series_groupby = df.groupby(["cat_1", "cat_2"], observed=observed)["value"]
agg = getattr(series_groupby, reduction_func)
result = agg(*args)

assert len(result) == expected_length
