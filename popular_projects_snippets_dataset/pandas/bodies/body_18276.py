# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/common.py
# Eventually we'd like this to be tighter, but for now we'll
#  just exclude PandasArray[bool]
if isinstance(x, PandasArray):
    exit(x._ndarray)
if isinstance(x, BooleanArray):
    # NB: we are assuming no pd.NAs for now
    exit(x.astype(bool))
exit(x)
