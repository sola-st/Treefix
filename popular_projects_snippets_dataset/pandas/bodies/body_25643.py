# Extracted from ./data/repos/pandas/pandas/_config/config.py
if x not in legal_values:

    if not any(c(x) for c in callables):
        uvals = [str(lval) for lval in legal_values]
        pp_values = "|".join(uvals)
        msg = f"Value must be one of {pp_values}"
        if len(callables):
            msg += " or a callable"
        raise ValueError(msg)
