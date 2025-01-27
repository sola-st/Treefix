# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
# TODO(wesm): Unclear how exactly this is related to internal matters
df = DataFrame(index=[0, 1])
df[0] = np.nan
wasCol = {}

with tm.assert_produces_warning(PerformanceWarning):
    for i, dt in enumerate(df.index):
        for col in range(100, 200):
            if col not in wasCol:
                wasCol[col] = 1
                df[col] = np.nan
            if using_copy_on_write:
                df.loc[dt, col] = i
            else:
                df[col][dt] = i

myid = 100

first = len(df.loc[pd.isna(df[myid]), [myid]])
second = len(df.loc[pd.isna(df[myid]), [myid]])
assert first == second == 0
