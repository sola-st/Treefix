# Extracted from ./data/repos/pandas/pandas/tests/extension/base/interface.py
# If your `isna` returns an ExtensionArray, you must also implement
# _reduce. At the *very* least, you must implement any and all
na = data_missing.isna()
if is_extension_array_dtype(na):
    assert na._reduce("any")
    assert na.any()

    assert not na._reduce("all")
    assert not na.all()

    assert na.dtype._is_boolean
