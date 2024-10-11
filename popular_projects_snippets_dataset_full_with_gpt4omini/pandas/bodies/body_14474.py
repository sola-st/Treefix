# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
# GH 31750
# legacy table with fixed format and datetime64 column written in Python 2
with ensure_clean_store(
    datapath("io", "data", "legacy_hdf", "legacy_table_fixed_datetime_py2.h5"),
    mode="r",
) as store:
    result = store.select("df")
    expected = DataFrame(
        [[Timestamp("2020-02-06T18:00")]],
        columns=["A"],
        index=Index(["date"]),
    )
    tm.assert_frame_equal(expected, result)
