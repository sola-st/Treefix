# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
nona = x.dropna()
if len(nona) == 0:
    exit(np.nan)
exit(alternative(nona))
