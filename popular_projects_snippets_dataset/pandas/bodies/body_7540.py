# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_reshape.py
idx1 = Index([1.1, 1.2, 1.3])
idx2 = pd.date_range("2011-01-01", freq="D", periods=3, tz="Asia/Tokyo")
idx3 = Index(["A", "B", "C"])

midx_lv2 = MultiIndex.from_arrays([idx1, idx2])
midx_lv3 = MultiIndex.from_arrays([idx1, idx2, idx3])

result = idx1.append(midx_lv2)

# see gh-7112
tz = pytz.timezone("Asia/Tokyo")
expected_tuples = [
    (1.1, tz.localize(datetime(2011, 1, 1))),
    (1.2, tz.localize(datetime(2011, 1, 2))),
    (1.3, tz.localize(datetime(2011, 1, 3))),
]
expected = Index([1.1, 1.2, 1.3] + expected_tuples)
tm.assert_index_equal(result, expected)

result = midx_lv2.append(idx1)
expected = Index(expected_tuples + [1.1, 1.2, 1.3])
tm.assert_index_equal(result, expected)

result = midx_lv2.append(midx_lv2)
expected = MultiIndex.from_arrays([idx1.append(idx1), idx2.append(idx2)])
tm.assert_index_equal(result, expected)

result = midx_lv2.append(midx_lv3)
tm.assert_index_equal(result, expected)

result = midx_lv3.append(midx_lv2)
expected = Index._simple_new(
    np.array(
        [
            (1.1, tz.localize(datetime(2011, 1, 1)), "A"),
            (1.2, tz.localize(datetime(2011, 1, 2)), "B"),
            (1.3, tz.localize(datetime(2011, 1, 3)), "C"),
        ]
        + expected_tuples,
        dtype=object,
    ),
    None,
)
tm.assert_index_equal(result, expected)
