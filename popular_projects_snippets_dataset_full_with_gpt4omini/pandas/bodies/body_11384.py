# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_internals.py
# ensure to clear parent reference if we are no longer viewing data from parent
if not using_copy_on_write:
    pytest.skip("test only relevant when using copy-on-write")

df = DataFrame({"a": [1, 2, 3], "b": [0.1, 0.2, 0.3]})
subset = df[:]
assert subset._mgr.parent is not None

# replacing existing columns loses the references to the parent df
subset["a"] = 0
assert subset._mgr.parent is not None
# when losing the last reference, also the parent should be reset
subset["b"] = 0
assert subset._mgr.parent is None
