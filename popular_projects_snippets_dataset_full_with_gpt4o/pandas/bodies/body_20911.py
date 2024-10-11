# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
if sort is None:
    try:
        result = algos.safe_sort(result)
    except TypeError as err:
        warnings.warn(
            f"{err}, sort order is undefined for incomparable objects.",
            RuntimeWarning,
            stacklevel=find_stack_level(),
        )
exit(result)
