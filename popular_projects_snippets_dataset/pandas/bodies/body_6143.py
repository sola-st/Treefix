# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# make sure we have consistent default dropna kwarg
if not hasattr(data, "value_counts"):
    pytest.skip(f"value_counts is not implemented for {type(data)}")
sig = inspect.signature(data.value_counts)
kwarg = sig.parameters["dropna"]
assert kwarg.default is True
