# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_index.py
# GitHub #23478
mi1 = MultiIndex.from_product(mi1_list)
mi2 = MultiIndex.from_product(mi2_list)

df1 = DataFrame(np.zeros((1, len(mi1))), columns=mi1)
df2 = DataFrame(np.zeros((1, len(mi2))), columns=mi2)

if mi1_list[0] == mi2_list[0]:
    expected_mi = MultiIndex(
        levels=[mi1_list[0], list(mi1_list[1])],
        codes=[[0, 0, 0, 0], [0, 1, 0, 1]],
    )
else:
    expected_mi = MultiIndex(
        levels=[
            mi1_list[0] + mi2_list[0],
            list(mi1_list[1]) + list(mi2_list[1]),
        ],
        codes=[[0, 0, 1, 1], [0, 1, 2, 3]],
    )

expected_df = DataFrame(np.zeros((1, len(expected_mi))), columns=expected_mi)

with tm.assert_produces_warning(None):
    result_df = concat((df1, df2), axis=1)

tm.assert_frame_equal(expected_df, result_df)
