# Extracted from ./data/repos/pandas/pandas/tests/util/test_util.py
args = ("io", "data", "csv", "iris.csv")

result = datapath(*args)
expected = os.path.join(os.path.dirname(os.path.dirname(__file__)), *args)

assert result == expected
