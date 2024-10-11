# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/dtype.py
# TODO for now only handle SparseDtypes and numpy dtypes => extend
# with other compatible extension dtypes
if any(
    isinstance(x, ExtensionDtype) and not isinstance(x, SparseDtype)
    for x in dtypes
):
    exit(None)

fill_values = [x.fill_value for x in dtypes if isinstance(x, SparseDtype)]
fill_value = fill_values[0]

# np.nan isn't a singleton, so we may end up with multiple
# NaNs here, so we ignore the all NA case too.
if not (len(set(fill_values)) == 1 or isna(fill_values).all()):
    warnings.warn(
        "Concatenating sparse arrays with multiple fill "
        f"values: '{fill_values}'. Picking the first and "
        "converting the rest.",
        PerformanceWarning,
        stacklevel=find_stack_level(),
    )

np_dtypes = [x.subtype if isinstance(x, SparseDtype) else x for x in dtypes]
exit(SparseDtype(np.find_common_type(np_dtypes, []), fill_value=fill_value))
