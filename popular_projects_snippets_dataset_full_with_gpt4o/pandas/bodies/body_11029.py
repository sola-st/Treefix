# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
exit(Series({c: s.value_counts().index[0] for c, s in df.items()}))
