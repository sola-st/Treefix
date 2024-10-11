# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
idx1 = PeriodIndex(
    ["2014-01", "2014-01", "2014-02", "2014-02", "2014-03", "2014-03"], freq="M"
)

cat1 = Categorical(idx1)
str(cat1)
exp_arr = np.array([0, 0, 1, 1, 2, 2], dtype=np.int8)
exp_idx = PeriodIndex(["2014-01", "2014-02", "2014-03"], freq="M")
tm.assert_numpy_array_equal(cat1._codes, exp_arr)
tm.assert_index_equal(cat1.categories, exp_idx)

idx2 = PeriodIndex(
    ["2014-03", "2014-03", "2014-02", "2014-01", "2014-03", "2014-01"], freq="M"
)
cat2 = Categorical(idx2, ordered=True)
str(cat2)
exp_arr = np.array([2, 2, 1, 0, 2, 0], dtype=np.int8)
exp_idx2 = PeriodIndex(["2014-01", "2014-02", "2014-03"], freq="M")
tm.assert_numpy_array_equal(cat2._codes, exp_arr)
tm.assert_index_equal(cat2.categories, exp_idx2)

idx3 = PeriodIndex(
    [
        "2013-12",
        "2013-11",
        "2013-10",
        "2013-09",
        "2013-08",
        "2013-07",
        "2013-05",
    ],
    freq="M",
)
cat3 = Categorical(idx3, ordered=True)
exp_arr = np.array([6, 5, 4, 3, 2, 1, 0], dtype=np.int8)
exp_idx = PeriodIndex(
    [
        "2013-05",
        "2013-07",
        "2013-08",
        "2013-09",
        "2013-10",
        "2013-11",
        "2013-12",
    ],
    freq="M",
)
tm.assert_numpy_array_equal(cat3._codes, exp_arr)
tm.assert_index_equal(cat3.categories, exp_idx)
