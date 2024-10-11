# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
if not using_copy_on_write:
    request.node.add_marker(pytest.mark.xfail(reason="Unclear behavior."))
# NDFrame.__getitem__ will cache the first df['A']. May need to
# invalidate that cache? Update the cached entries?
df = pd.DataFrame({"A": [0]}).set_flags(allows_duplicate_labels=False)
assert df["A"].flags.allows_duplicate_labels is False
df.flags.allows_duplicate_labels = True
assert df["A"].flags.allows_duplicate_labels is True
