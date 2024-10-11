# Extracted from ./data/repos/tensorflow/tensorflow/python/compat/compat.py
"""Update the base date to compare in forward_compatible function."""

global _FORWARD_COMPATIBILITY_DATE_NUMBER

if date_to_override:
    date = date_to_override
else:
    date = _FORWARD_COMPATIBILITY_HORIZON
    delta_days = os.getenv(_FORWARD_COMPATIBILITY_DELTA_DAYS_VAR_NAME)
    if delta_days:
        date += datetime.timedelta(days=int(delta_days))

if date < _FORWARD_COMPATIBILITY_HORIZON:
    logging.warning("Trying to set the forward compatibility date to the past"
                    " date %s. This will be ignored by TensorFlow." % (date))
    exit()
_FORWARD_COMPATIBILITY_DATE_NUMBER = _date_to_date_number(
    date.year, date.month, date.day)
