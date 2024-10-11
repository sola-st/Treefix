# Extracted from ./data/repos/pandas/pandas/_config/config.py

callables = [c for c in legal_values if callable(c)]
legal_values = [c for c in legal_values if not callable(c)]

def inner(x) -> None:
    if x not in legal_values:

        if not any(c(x) for c in callables):
            uvals = [str(lval) for lval in legal_values]
            pp_values = "|".join(uvals)
            msg = f"Value must be one of {pp_values}"
            if len(callables):
                msg += " or a callable"
            raise ValueError(msg)

exit(inner)
