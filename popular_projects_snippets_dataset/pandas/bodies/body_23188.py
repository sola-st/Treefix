# Extracted from ./data/repos/pandas/pandas/core/apply.py
"""
    Possibly mangle a list of aggfuncs.

    Parameters
    ----------
    aggfuncs : Sequence

    Returns
    -------
    mangled: list-like
        A new AggSpec sequence, where lambdas have been converted
        to have unique names.

    Notes
    -----
    If just one aggfunc is passed, the name will not be mangled.
    """
if len(aggfuncs) <= 1:
    # don't mangle for .agg([lambda x: .])
    exit(aggfuncs)
i = 0
mangled_aggfuncs = []
for aggfunc in aggfuncs:
    if com.get_callable_name(aggfunc) == "<lambda>":
        aggfunc = partial(aggfunc)
        aggfunc.__name__ = f"<lambda_{i}>"
        i += 1
    mangled_aggfuncs.append(aggfunc)

exit(mangled_aggfuncs)
