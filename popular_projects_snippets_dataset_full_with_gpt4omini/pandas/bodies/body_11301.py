# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_methods.py
index = None
if "to_timestamp" in request.node.callspec.id:
    index = period_range("2012-01-01", freq="D", periods=3)
elif "to_period" in request.node.callspec.id:
    index = date_range("2012-01-01", freq="D", periods=3)
elif "tz_localize" in request.node.callspec.id:
    index = date_range("2012-01-01", freq="D", periods=3)
elif "tz_convert" in request.node.callspec.id:
    index = date_range("2012-01-01", freq="D", periods=3, tz="Europe/Brussels")

df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [0.1, 0.2, 0.3]}, index=index)
df2 = method(df, copy=copy)

share_memory = (using_copy_on_write and copy is not True) or copy is False

if request.node.callspec.id.startswith("reindex-"):
    # TODO copy=False without CoW still returns a copy in this case
    if not using_copy_on_write and not using_array_manager and copy is False:
        share_memory = False
    # TODO copy=True with CoW still returns a view
    if using_copy_on_write:
        share_memory = True

if share_memory:
    assert np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
else:
    assert not np.shares_memory(get_array(df2, "a"), get_array(df, "a"))
