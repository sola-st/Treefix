# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
# GH 16781

# tests reading a PeriodIndex DataFrame written in Python2 in Python3

# the file was generated in Python 2.7 like so:
#
# df = DataFrame([1.,2,3], index=pd.PeriodIndex(
#              ['2015-01-01', '2015-01-02', '2015-01-05'], freq='B'))
# df.to_hdf('periodindex_0.20.1_x86_64_darwin_2.7.13.h5', 'p')

expected = DataFrame(
    [1.0, 2, 3],
    index=pd.PeriodIndex(["2015-01-01", "2015-01-02", "2015-01-05"], freq="B"),
)

with ensure_clean_store(
    datapath(
        "io", "data", "legacy_hdf", "periodindex_0.20.1_x86_64_darwin_2.7.13.h5"
    ),
    mode="r",
) as store:
    result = store["p"]
    tm.assert_frame_equal(result, expected)
