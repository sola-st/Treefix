# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 12017
aggs = {"D": "sum", "E": "mean"}

pivot_values_list = pivot_table(
    data, index=["A"], values=list(aggs.keys()), aggfunc=aggs
)

pivot_values_keys = pivot_table(
    data, index=["A"], values=aggs.keys(), aggfunc=aggs
)
tm.assert_frame_equal(pivot_values_keys, pivot_values_list)

agg_values_gen = (value for value in aggs)
pivot_values_gen = pivot_table(
    data, index=["A"], values=agg_values_gen, aggfunc=aggs
)
tm.assert_frame_equal(pivot_values_gen, pivot_values_list)
