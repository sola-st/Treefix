# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
message = "module 'pandas' has no attribute 'thing'"
with pytest.raises(AttributeError, match=message):
    df.eval("@pd.thing")
