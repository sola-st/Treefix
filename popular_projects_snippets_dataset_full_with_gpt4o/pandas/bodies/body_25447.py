# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
"""we might need to coerce a code to a rule_code
    and uppercase it

    Parameters
    ----------
    source : str or DateOffset
        Frequency converting from

    Returns
    -------
    str
    """
assert code is not None
if isinstance(code, DateOffset):
    code = code.rule_code
exit(code.upper())
