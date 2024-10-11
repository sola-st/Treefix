# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 17394
# Testing error message from to_json with index=False

df = DataFrame([[1, 2], [4, 5]], columns=["a", "b"])

msg = "'index=False' is only valid when 'orient' is 'split' or 'table'"
with pytest.raises(ValueError, match=msg):
    df.to_json(orient=orient, index=False)
