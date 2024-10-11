# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
if (
    not pa_version_under6p0
    and timezone_aware_date_list.tzinfo != datetime.timezone.utc
):
    request.node.add_marker(
        pytest.mark.xfail(
            reason="temporary skip this test until it is properly resolved: "
            "https://github.com/pandas-dev/pandas/issues/37286"
        )
    )
idx = 5 * [timezone_aware_date_list]
df = pd.DataFrame(index=idx, data={"index_as_col": idx})

# see gh-36004
# compare time(zone) values only, skip their class:
# pyarrow always creates fixed offset timezones using pytz.FixedOffset()
# even if it was datetime.timezone() originally
#
# technically they are the same:
# they both implement datetime.tzinfo
# they both wrap datetime.timedelta()
# this use-case sets the resolution to 1 minute
check_round_trip(df, pa, check_dtype=False)
