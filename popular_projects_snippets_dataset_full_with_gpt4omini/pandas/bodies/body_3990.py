# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
obj = DataFrame({"A": [1, 2]})
key = (0, 0)
if frame_or_series is Series:
    obj = obj["A"]
    key = 0

result = obj.set_flags(allows_duplicate_labels=allows_duplicate_labels)

if allows_duplicate_labels is None:
    # We don't update when it's not provided
    assert result.flags.allows_duplicate_labels is True
else:
    assert result.flags.allows_duplicate_labels is allows_duplicate_labels

# We made a copy
assert obj is not result

# We didn't mutate obj
assert obj.flags.allows_duplicate_labels is True

# But we didn't copy data
if frame_or_series is Series:
    assert np.may_share_memory(obj.values, result.values)
else:
    assert np.may_share_memory(obj["A"].values, result["A"].values)

result.iloc[key] = 0
if using_copy_on_write:
    assert obj.iloc[key] == 1
else:
    assert obj.iloc[key] == 0
    # set back to 1 for test below
    result.iloc[key] = 1

# Now we do copy.
result = obj.set_flags(
    copy=True, allows_duplicate_labels=allows_duplicate_labels
)
result.iloc[key] = 10
assert obj.iloc[key] == 1
