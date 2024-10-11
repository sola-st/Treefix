# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 13139
with pytest.raises(ValueError, match="expr cannot be an empty string"):
    pd.eval("", engine=engine, parser=parser)
