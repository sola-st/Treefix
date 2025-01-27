# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
msg = "Failed to parse backticks"
with pytest.raises(SyntaxError, match=msg):
    df.query("`foo#bar` > 4")
