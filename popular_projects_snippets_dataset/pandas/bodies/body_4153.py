# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
# GH 13139
df = DataFrame({"A": [1, 2, 3]})

msg = "expr cannot be an empty string"
with pytest.raises(ValueError, match=msg):
    df.query("")
