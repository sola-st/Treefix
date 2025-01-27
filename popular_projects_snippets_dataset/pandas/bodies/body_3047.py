# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
df = DataFrame({"A": [0, 1]})
msg = "orient 'xinvalid' not understood"
with pytest.raises(ValueError, match=msg):
    df.to_dict(orient="xinvalid")
