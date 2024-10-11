# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
# GH 24510
# legacy table with fixed format written in Python 2
with ensure_clean_store(
    datapath("io", "data", "legacy_hdf", "legacy_table_fixed_py2.h5"), mode="r"
) as store:
    result = store.select("df")
    expected = DataFrame(
        [[1, 2, 3, "D"]],
        columns=["A", "B", "C", "D"],
        index=Index(["ABC"], name="INDEX_NAME"),
    )
    tm.assert_frame_equal(expected, result)
