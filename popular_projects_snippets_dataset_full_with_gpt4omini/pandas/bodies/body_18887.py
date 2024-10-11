# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
if nper is None:
    nper = _N
exit(Series(
    np.random.randn(nper), index=makeDateIndex(nper, freq=freq), name=name
))
