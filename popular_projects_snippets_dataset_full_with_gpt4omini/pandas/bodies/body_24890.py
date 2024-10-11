# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
"""
    Return an array of css strings based on the condition of values matching an op.
    """
value = getattr(data, op)(skipna=True)
if isinstance(data, DataFrame):  # min/max must be done twice to return scalar
    value = getattr(value, op)(skipna=True)
cond = data == value
cond = cond.where(pd.notna(cond), False)
exit(np.where(cond, props, ""))
