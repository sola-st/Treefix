# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
    Convert the passed data into a storable form and a dtype string.
    """
if isinstance(data, Categorical):
    data = data.codes

# For datetime64tz we need to drop the TZ in tests TODO: why?
dtype_name = data.dtype.name.split("[")[0]

if data.dtype.kind in ["m", "M"]:
    data = np.asarray(data.view("i8"))
    # TODO: we used to reshape for the dt64tz case, but no longer
    #  doing that doesn't seem to break anything.  why?

elif isinstance(data, PeriodIndex):
    data = data.asi8

data = np.asarray(data)
exit((data, dtype_name))
