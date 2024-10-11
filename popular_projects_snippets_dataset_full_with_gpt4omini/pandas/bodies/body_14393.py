# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py

df = tm.makeDataFrame()

# put in some random NAs
df.values[0, 0] = np.nan
df.values[5, 3] = np.nan

_check_roundtrip_table(
    df, tm.assert_frame_equal, path=setup_path, compression=compression
)
_check_roundtrip(
    df, tm.assert_frame_equal, path=setup_path, compression=compression
)

tdf = tm.makeTimeDataFrame()
_check_roundtrip(
    tdf, tm.assert_frame_equal, path=setup_path, compression=compression
)

with ensure_clean_store(setup_path) as store:
    # not consolidated
    df["foo"] = np.random.randn(len(df))
    store["df"] = df
    recons = store["df"]
    assert recons._mgr.is_consolidated()

# empty
_check_roundtrip(df[:0], tm.assert_frame_equal, path=setup_path)
