# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict_of_blocks.py
if using_copy_on_write:
    request.node.add_marker(pytest.mark.xfail(reason="CoW - not yet implemented"))
# Calling to_dict_of_blocks should not poison item_cache
df = DataFrame({"a": [1, 2, 3, 4], "b": ["a", "b", "c", "d"]})
df["c"] = PandasArray(np.array([1, 2, None, 3], dtype=object))
mgr = df._mgr
assert len(mgr.blocks) == 3  # i.e. not consolidated

ser = df["b"]  # populations item_cache["b"]

df._to_dict_of_blocks()

if using_copy_on_write:
    # TODO(CoW) we should disallow this, so `df` doesn't get updated,
    # this currently still updates df, so this test fails
    ser.values[0] = "foo"
    assert df.loc[0, "b"] == "a"
else:
    # Check that the to_dict_of_blocks didn't break link between ser and df
    ser.values[0] = "foo"
    assert df.loc[0, "b"] == "foo"

    assert df["b"] is ser
