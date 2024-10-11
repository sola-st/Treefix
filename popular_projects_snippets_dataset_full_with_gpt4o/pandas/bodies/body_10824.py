# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH 23865
# GH 27075
# Ensure that df.groupby, when 'by' is two Categorical variables,
# does not return the categories that are not in df when observed=True
if reduction_func == "ngroup":
    pytest.skip("ngroup does not return the Categories on the index")

df = DataFrame(
    {
        "cat_1": Categorical(list("AABB"), categories=list("ABC")),
        "cat_2": Categorical(list("1111"), categories=list("12")),
        "value": [0.1, 0.1, 0.1, 0.1],
    }
)
unobserved_cats = [("A", "2"), ("B", "2"), ("C", "1"), ("C", "2")]

df_grp = df.groupby(["cat_1", "cat_2"], observed=True)

args = get_groupby_method_args(reduction_func, df)
res = getattr(df_grp, reduction_func)(*args)

for cat in unobserved_cats:
    assert cat not in res.index
