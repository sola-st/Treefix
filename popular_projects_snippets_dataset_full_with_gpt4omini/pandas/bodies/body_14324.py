# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_timezones.py
# legacy from < 0.17.0
# 8260
expected = DataFrame(
    {
        "A": Timestamp("20130102", tz="US/Eastern"),
        "B": Timestamp("20130603", tz="CET"),
    },
    index=range(5),
)
with ensure_clean_store(
    datapath("io", "data", "legacy_hdf", "datetimetz_object.h5"), mode="r"
) as store:
    result = store["df"]
    tm.assert_frame_equal(result, expected)
