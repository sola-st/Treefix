# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
# issue: 24925
# legacy table written in Python 2
with ensure_clean_store(
    datapath("io", "data", "legacy_hdf", "legacy_table_py2.h5"), mode="r"
) as store:
    result = store.select("table")

expected = DataFrame({"a": ["a", "b"], "b": [2, 3]})
tm.assert_frame_equal(expected, result)
