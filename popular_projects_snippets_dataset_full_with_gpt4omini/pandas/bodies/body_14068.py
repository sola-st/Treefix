# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# representing infs poses no problems
df = DataFrame({"foo": [-np.inf, np.inf]})
repr(df)
