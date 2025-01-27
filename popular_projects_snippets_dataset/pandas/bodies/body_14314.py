# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_timezones.py
# as columns

# Single-tzinfo, no DST transition
df_est = DataFrame(
    {
        "A": [
            Timestamp("20130102 2:00:00", tz=gettz("US/Eastern"))
            + timedelta(hours=1) * i
            for i in range(5)
        ]
    }
)

# frame with all columns having same tzinfo, but different sides
#  of DST transition
df_crosses_dst = DataFrame(
    {
        "A": Timestamp("20130102", tz=gettz("US/Eastern")),
        "B": Timestamp("20130603", tz=gettz("US/Eastern")),
    },
    index=range(5),
)

df_mixed_tz = DataFrame(
    {
        "A": Timestamp("20130102", tz=gettz("US/Eastern")),
        "B": Timestamp("20130102", tz=gettz("EET")),
    },
    index=range(5),
)

df_different_tz = DataFrame(
    {
        "A": Timestamp("20130102", tz=gettz("US/Eastern")),
        "B": Timestamp("20130102", tz=gettz("CET")),
    },
    index=range(5),
)

with ensure_clean_store(setup_path) as store:

    _maybe_remove(store, "df_tz")
    store.append("df_tz", df_est, data_columns=["A"])
    result = store["df_tz"]
    _compare_with_tz(result, df_est)
    tm.assert_frame_equal(result, df_est)

    # select with tz aware
    expected = df_est[df_est.A >= df_est.A[3]]
    result = store.select("df_tz", where="A>=df_est.A[3]")
    _compare_with_tz(result, expected)

    # ensure we include dates in DST and STD time here.
    _maybe_remove(store, "df_tz")
    store.append("df_tz", df_crosses_dst)
    result = store["df_tz"]
    _compare_with_tz(result, df_crosses_dst)
    tm.assert_frame_equal(result, df_crosses_dst)

    msg = (
        r"invalid info for \[values_block_1\] for \[tz\], "
        r"existing_value \[(dateutil/.*)?US/Eastern\] "
        r"conflicts with new value \[(dateutil/.*)?EET\]"
    )
    with pytest.raises(ValueError, match=msg):
        store.append("df_tz", df_mixed_tz)

    # this is ok
    _maybe_remove(store, "df_tz")
    store.append("df_tz", df_mixed_tz, data_columns=["A", "B"])
    result = store["df_tz"]
    _compare_with_tz(result, df_mixed_tz)
    tm.assert_frame_equal(result, df_mixed_tz)

    # can't append with diff timezone
    msg = (
        r"invalid info for \[B\] for \[tz\], "
        r"existing_value \[(dateutil/.*)?EET\] "
        r"conflicts with new value \[(dateutil/.*)?CET\]"
    )
    with pytest.raises(ValueError, match=msg):
        store.append("df_tz", df_different_tz)
