# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# test all parameters:
# - Use column, array or function as by= parameter
# - Whether or not to normalize
# - Whether or not to sort and how
# - Whether or not to use the groupby as an index
# - 3-way compare against:
#   - apply with :meth:`~DataFrame.value_counts`
#   - `~SeriesGroupBy.value_counts`
by = {
    "column": "country",
    "array": education_df["country"].values,
    "function": lambda x: education_df["country"][x] == "US",
}[groupby]

gp = education_df.groupby(by=by, as_index=as_index)
result = gp[["gender", "education"]].value_counts(
    normalize=normalize, sort=sort, ascending=ascending
)
if frame:
    # compare against apply with DataFrame value_counts
    expected = gp.apply(
        _frame_value_counts, ["gender", "education"], normalize, sort, ascending
    )

    if as_index:
        tm.assert_series_equal(result, expected)
    else:
        name = "proportion" if normalize else "count"
        expected = expected.reset_index().rename({0: name}, axis=1)
        if groupby == "column":
            expected = expected.rename({"level_0": "country"}, axis=1)
            expected["country"] = np.where(expected["country"], "US", "FR")
        elif groupby == "function":
            expected["level_0"] = expected["level_0"] == 1
        else:
            expected["level_0"] = np.where(expected["level_0"], "US", "FR")
        tm.assert_frame_equal(result, expected)
else:
    # compare against SeriesGroupBy value_counts
    education_df["both"] = education_df["gender"] + "-" + education_df["education"]
    expected = gp["both"].value_counts(
        normalize=normalize, sort=sort, ascending=ascending
    )
    expected.name = None
    if as_index:
        index_frame = expected.index.to_frame(index=False)
        index_frame["gender"] = index_frame["both"].str.split("-").str.get(0)
        index_frame["education"] = index_frame["both"].str.split("-").str.get(1)
        del index_frame["both"]
        index_frame = index_frame.rename({0: None}, axis=1)
        expected.index = MultiIndex.from_frame(index_frame)
        tm.assert_series_equal(result, expected)
    else:
        expected.insert(1, "gender", expected["both"].str.split("-").str.get(0))
        expected.insert(2, "education", expected["both"].str.split("-").str.get(1))
        del expected["both"]
        tm.assert_frame_equal(result, expected)
