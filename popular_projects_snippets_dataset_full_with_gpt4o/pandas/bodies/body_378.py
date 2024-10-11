# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py

msg = 'For argument "inplace" expected type bool, received type'
with pytest.raises(ValueError, match=msg):
    pd.eval("2+2", inplace=value)
