# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 25823
event = Series({"a": "hello"})
assert pd.eval(f"{event.str.match('hello').a}")
assert pd.eval(f"{event.str.match('hello').a and event.str.match('hello').a}")
