# Extracted from ./data/repos/pandas/pandas/tests/frame/test_cumulative.py
datetime_frame.iloc[5:10, 0] = np.nan
datetime_frame.iloc[10:15, 1] = np.nan
datetime_frame.iloc[15:, 2] = np.nan

# ints
df = datetime_frame.fillna(0).astype(int)
df.cumprod(0)
df.cumprod(1)

# ints32
df = datetime_frame.fillna(0).astype(np.int32)
df.cumprod(0)
df.cumprod(1)
