# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
# GH 11485
df = DataFrame({"A": [1, 2, 3], "B": ["a", "b", "b"]})

msg = "expr must be a string to be evaluated"
with pytest.raises(ValueError, match=msg):
    df.query(lambda x: x.B == "b")

with pytest.raises(ValueError, match=msg):
    df.query(111)
