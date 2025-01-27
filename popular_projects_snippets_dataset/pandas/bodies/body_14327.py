# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_timezones.py
# The test HDF5 file was created in Python 2, but could not be read in
# Python 3.
#
# GH26443
index = [Timestamp("2019-01-01T18:00").tz_localize("America/New_York")]
expected = DataFrame({"data": 123}, index=index)
with ensure_clean_store(
    datapath("io", "data", "legacy_hdf", "gh26443.h5"), mode="r"
) as store:
    result = store["key"]
    tm.assert_frame_equal(result, expected)
