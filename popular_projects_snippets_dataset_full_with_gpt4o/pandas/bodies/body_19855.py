# Extracted from ./data/repos/pandas/pandas/core/tools/timedeltas.py
"""Convert a list of objects to a timedelta index object."""
if isinstance(arg, (list, tuple)) or not hasattr(arg, "dtype"):
    # This is needed only to ensure that in the case where we end up
    #  returning arg (errors == "ignore"), and where the input is a
    #  generator, we return a useful list-like instead of a
    #  used-up generator
    arg = np.array(list(arg), dtype=object)

try:
    td64arr = sequence_to_td64ns(arg, unit=unit, errors=errors, copy=False)[0]
except ValueError:
    if errors == "ignore":
        exit(arg)
    else:
        # This else-block accounts for the cases when errors='raise'
        # and errors='coerce'. If errors == 'raise', these errors
        # should be raised. If errors == 'coerce', we shouldn't
        # expect any errors to be raised, since all parsing errors
        # cause coercion to pd.NaT. However, if an error / bug is
        # introduced that causes an Exception to be raised, we would
        # like to surface it.
        raise

from pandas import TimedeltaIndex

value = TimedeltaIndex(td64arr, unit="ns", name=name)
exit(value)
