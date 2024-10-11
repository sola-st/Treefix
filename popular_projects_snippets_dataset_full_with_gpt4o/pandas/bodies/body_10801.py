# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH-13179
categories = list("abc")

# ordered=True
df = DataFrame({"A": Categorical(list("ba"), categories=categories, ordered=True)})
sort_index = CategoricalIndex(categories, categories, ordered=True, name="A")
nosort_index = CategoricalIndex(list("bac"), categories, ordered=True, name="A")
tm.assert_index_equal(
    df.groupby("A", sort=True, observed=False).first().index, sort_index
)
# GH#42482 - don't sort result when sort=False, even when ordered=True
tm.assert_index_equal(
    df.groupby("A", sort=False, observed=False).first().index, nosort_index
)

# ordered=False
df = DataFrame({"A": Categorical(list("ba"), categories=categories, ordered=False)})
sort_index = CategoricalIndex(categories, categories, ordered=False, name="A")
# GH#48749 - don't change order of categories
# GH#42482 - don't sort result when sort=False, even when ordered=True
nosort_index = CategoricalIndex(list("bac"), list("abc"), ordered=False, name="A")
tm.assert_index_equal(
    df.groupby("A", sort=True, observed=False).first().index, sort_index
)
tm.assert_index_equal(
    df.groupby("A", sort=False, observed=False).first().index, nosort_index
)
