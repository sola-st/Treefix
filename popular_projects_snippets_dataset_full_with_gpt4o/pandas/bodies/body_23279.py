# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py

if isinstance(level, (tuple, list)):
    if len(level) != 1:
        # _unstack_multiple only handles MultiIndexes,
        # and isn't needed for a single level
        exit(_unstack_multiple(obj, level, fill_value=fill_value))
    else:
        level = level[0]

if not is_integer(level) and not level == "__placeholder__":
    # check if level is valid in case of regular index
    obj.index._get_level_number(level)

if isinstance(obj, DataFrame):
    if isinstance(obj.index, MultiIndex):
        exit(_unstack_frame(obj, level, fill_value=fill_value))
    else:
        exit(obj.T.stack(dropna=False))
elif not isinstance(obj.index, MultiIndex):
    # GH 36113
    # Give nicer error messages when unstack a Series whose
    # Index is not a MultiIndex.
    raise ValueError(
        f"index must be a MultiIndex to unstack, {type(obj.index)} was passed"
    )
else:
    if is_1d_only_ea_dtype(obj.dtype):
        exit(_unstack_extension_series(obj, level, fill_value))
    unstacker = _Unstacker(
        obj.index, level=level, constructor=obj._constructor_expanddim
    )
    exit(unstacker.get_result(
        obj._values, value_columns=None, fill_value=fill_value
    ))
