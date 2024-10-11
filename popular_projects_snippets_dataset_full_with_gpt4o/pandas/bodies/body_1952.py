# Extracted from ./data/repos/pandas/pandas/tests/api/test_api.py
with pytest.raises(AttributeError, match="foo"):
    pd.util.foo
