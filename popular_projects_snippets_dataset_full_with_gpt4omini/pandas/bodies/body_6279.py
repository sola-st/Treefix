# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
# GH#44514
df = pd.DataFrame({"A": data})

# Avoiding using_array_manager fixture
#  https://github.com/pandas-dev/pandas/pull/44514#discussion_r754002410
using_array_manager = isinstance(df._mgr, pd.core.internals.ArrayManager)
using_copy_on_write = pd.options.mode.copy_on_write

blk_data = df._mgr.arrays[0]

orig = df.copy()

df.iloc[:] = df
self.assert_frame_equal(df, orig)

df.iloc[:-1] = df.iloc[:-1]
self.assert_frame_equal(df, orig)

df.iloc[:] = df.values
self.assert_frame_equal(df, orig)
if not using_array_manager and not using_copy_on_write:
    # GH#33457 Check that this setting occurred in-place
    # FIXME(ArrayManager): this should work there too
    assert df._mgr.arrays[0] is blk_data

df.iloc[:-1] = df.values[:-1]
self.assert_frame_equal(df, orig)
