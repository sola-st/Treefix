# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
msg = r"(Could not convert ).*( to a valid Python identifier.)"
with pytest.raises(SyntaxError, match=msg):
    df.query("`☺` > 4")
