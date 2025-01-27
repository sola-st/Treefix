# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
# GH 40164
kwargs = {arg: 1, "adjust": adjust, "ignore_na": ignore_na}
ewm = DataFrame({"A": range(1), "B": range(1)}).ewm(**kwargs)
expected = {attr: getattr(ewm, attr) for attr in ewm._attributes}
ewm_slice = ewm["A"]
result = {attr: getattr(ewm, attr) for attr in ewm_slice._attributes}
assert result == expected
