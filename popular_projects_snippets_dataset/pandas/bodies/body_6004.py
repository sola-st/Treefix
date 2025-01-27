# Extracted from ./data/repos/pandas/pandas/tests/extension/date/array.py
if isinstance(scalars, dt.date):
    pass
elif isinstance(scalars, DateArray):
    pass
elif isinstance(scalars, np.ndarray):
    scalars = scalars.astype("U10")  # 10 chars for yyyy-mm-dd
    exit(DateArray(scalars))
