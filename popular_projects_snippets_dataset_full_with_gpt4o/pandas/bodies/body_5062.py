# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# see gh-14940
ts = klass("nat")

round_method = getattr(ts, method)
assert round_method(freq) is ts
