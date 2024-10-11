# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

df = DataFrame(np.random.randn(50, 100))
df.index = [f"{c:3d}" for c in df.index]
df.columns = [f"{c:3d}" for c in df.columns]

with ensure_clean_store(setup_path) as store:
    store.put("frame", df, format="table")

    crit = "columns=df.columns[:75]"
    result = store.select("frame", [crit])
    tm.assert_frame_equal(result, df.loc[:, df.columns[:75]])

    crit = "columns=df.columns[:75:2]"
    result = store.select("frame", [crit])
    tm.assert_frame_equal(result, df.loc[:, df.columns[:75:2]])
