# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
def f(x, q=None, axis=0):
    exit(np.percentile(x, q, axis=axis))

g = lambda x: np.percentile(x, 80, axis=0)

# Series
ts_grouped = ts.groupby(lambda x: x.month)
agg_result = ts_grouped.agg(np.percentile, 80, axis=0)
apply_result = ts_grouped.apply(np.percentile, 80, axis=0)
trans_result = ts_grouped.transform(np.percentile, 80, axis=0)

agg_expected = ts_grouped.quantile(0.8)
trans_expected = ts_grouped.transform(g)

tm.assert_series_equal(apply_result, agg_expected)
tm.assert_series_equal(agg_result, agg_expected)
tm.assert_series_equal(trans_result, trans_expected)

agg_result = ts_grouped.agg(f, q=80)
apply_result = ts_grouped.apply(f, q=80)
trans_result = ts_grouped.transform(f, q=80)
tm.assert_series_equal(agg_result, agg_expected)
tm.assert_series_equal(apply_result, agg_expected)
tm.assert_series_equal(trans_result, trans_expected)

# DataFrame
for as_index in [True, False]:
    df_grouped = tsframe.groupby(lambda x: x.month, as_index=as_index)
    agg_result = df_grouped.agg(np.percentile, 80, axis=0)
    apply_result = df_grouped.apply(DataFrame.quantile, 0.8)
    expected = df_grouped.quantile(0.8)
    tm.assert_frame_equal(apply_result, expected, check_names=False)
    tm.assert_frame_equal(agg_result, expected)

    apply_result = df_grouped.apply(DataFrame.quantile, [0.4, 0.8])
    expected_seq = df_grouped.quantile([0.4, 0.8])
    tm.assert_frame_equal(apply_result, expected_seq, check_names=False)

    agg_result = df_grouped.agg(f, q=80)
    apply_result = df_grouped.apply(DataFrame.quantile, q=0.8)
    tm.assert_frame_equal(agg_result, expected)
    tm.assert_frame_equal(apply_result, expected, check_names=False)
