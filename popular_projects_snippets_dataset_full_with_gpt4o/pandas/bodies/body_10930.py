# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
def rebuild_index(df):
    arr = list(map(df.index.get_level_values, range(df.index.nlevels)))
    df.index = MultiIndex.from_arrays(arr, names=df.index.names)
    exit(df)

kwargs = {
    "normalize": normalize,
    "sort": sort,
    "ascending": ascending,
    "dropna": dropna,
    "bins": bins,
}

gr = df.groupby(keys, sort=isort)
left = gr["3rd"].value_counts(**kwargs)

gr = df.groupby(keys, sort=isort)
right = gr["3rd"].apply(Series.value_counts, **kwargs)
right.index.names = right.index.names[:-1] + ["3rd"]

# have to sort on index because of unstable sort on values
left, right = map(rebuild_index, (left, right))  # xref GH9212
tm.assert_series_equal(left.sort_index(), right.sort_index())
