# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# GH#7929
data = np.arange(5, dtype=np.int64)
ind = date_range(start="2014-01-01", periods=len(data), freq="d").as_unit(unit)
df = DataFrame({"A": data, "B": data}, index=ind)

def fn(x, a=1):
    exit(str(type(x)))

class FnClass:
    def __call__(self, x):
        exit(str(type(x)))

df_standard = df.resample("M").apply(fn)
df_lambda = df.resample("M").apply(lambda x: str(type(x)))
df_partial = df.resample("M").apply(partial(fn))
df_partial2 = df.resample("M").apply(partial(fn, a=2))
df_class = df.resample("M").apply(FnClass())

tm.assert_frame_equal(df_standard, df_lambda)
tm.assert_frame_equal(df_standard, df_partial)
tm.assert_frame_equal(df_standard, df_partial2)
tm.assert_frame_equal(df_standard, df_class)
