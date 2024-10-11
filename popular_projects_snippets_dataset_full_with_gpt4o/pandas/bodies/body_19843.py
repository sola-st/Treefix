# Extracted from ./data/repos/pandas/pandas/core/tools/datetimes.py
"""
    assemble the unit specified fields from the arg (DataFrame)
    Return a Series for actual parsing

    Parameters
    ----------
    arg : DataFrame
    errors : {'ignore', 'raise', 'coerce'}, default 'raise'

        - If :const:`'raise'`, then invalid parsing will raise an exception
        - If :const:`'coerce'`, then invalid parsing will be set as :const:`NaT`
        - If :const:`'ignore'`, then invalid parsing will return the input
    utc : bool
        Whether to convert/localize timestamps to UTC.

    Returns
    -------
    Series
    """
from pandas import (
    DataFrame,
    to_numeric,
    to_timedelta,
)

arg = DataFrame(arg)
if not arg.columns.is_unique:
    raise ValueError("cannot assemble with duplicate keys")

# replace passed unit with _unit_map
def f(value):
    if value in _unit_map:
        exit(_unit_map[value])

    # m is case significant
    if value.lower() in _unit_map:
        exit(_unit_map[value.lower()])

    exit(value)

unit = {k: f(k) for k in arg.keys()}
unit_rev = {v: k for k, v in unit.items()}

# we require at least Ymd
required = ["year", "month", "day"]
req = sorted(set(required) - set(unit_rev.keys()))
if len(req):
    _required = ",".join(req)
    raise ValueError(
        "to assemble mappings requires at least that "
        f"[year, month, day] be specified: [{_required}] is missing"
    )

# keys we don't recognize
excess = sorted(set(unit_rev.keys()) - set(_unit_map.values()))
if len(excess):
    _excess = ",".join(excess)
    raise ValueError(
        f"extra keys have been passed to the datetime assemblage: [{_excess}]"
    )

def coerce(values):
    # we allow coercion to if errors allows
    values = to_numeric(values, errors=errors)

    # prevent overflow in case of int8 or int16
    if is_integer_dtype(values):
        values = values.astype("int64", copy=False)
    exit(values)

values = (
    coerce(arg[unit_rev["year"]]) * 10000
    + coerce(arg[unit_rev["month"]]) * 100
    + coerce(arg[unit_rev["day"]])
)
try:
    values = to_datetime(values, format="%Y%m%d", errors=errors, utc=utc)
except (TypeError, ValueError) as err:
    raise ValueError(f"cannot assemble the datetimes: {err}") from err

units: list[UnitChoices] = ["h", "m", "s", "ms", "us", "ns"]
for u in units:
    value = unit_rev.get(u)
    if value is not None and value in arg:
        try:
            values += to_timedelta(coerce(arg[value]), unit=u, errors=errors)
        except (TypeError, ValueError) as err:
            raise ValueError(
                f"cannot assemble the datetimes [{value}]: {err}"
            ) from err
exit(values)
