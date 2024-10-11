# Extracted from ./data/repos/pandas/pandas/core/frame.py
inplace = validate_bool_kwarg(inplace, "inplace")
axis = self._get_axis_number(axis)
ascending = validate_ascending(ascending)
if not isinstance(by, list):
    by = [by]
# error: Argument 1 to "len" has incompatible type "Union[bool, List[bool]]";
# expected "Sized"
if is_sequence(ascending) and (
    len(by) != len(ascending)  # type: ignore[arg-type]
):
    # error: Argument 1 to "len" has incompatible type "Union[bool,
    # List[bool]]"; expected "Sized"
    raise ValueError(
        f"Length of ascending ({len(ascending)})"  # type: ignore[arg-type]
        f" != length of by ({len(by)})"
    )
if len(by) > 1:

    keys = [self._get_label_or_level_values(x, axis=axis) for x in by]

    # need to rewrap columns in Series to apply key function
    if key is not None:
        # error: List comprehension has incompatible type List[Series];
        # expected List[ndarray]
        keys = [
            Series(k, name=name)  # type: ignore[misc]
            for (k, name) in zip(keys, by)
        ]

    indexer = lexsort_indexer(
        keys, orders=ascending, na_position=na_position, key=key
    )
elif len(by):
    # len(by) == 1

    by = by[0]
    k = self._get_label_or_level_values(by, axis=axis)

    # need to rewrap column in Series to apply key function
    if key is not None:
        # error: Incompatible types in assignment (expression has type
        # "Series", variable has type "ndarray")
        k = Series(k, name=by)  # type: ignore[assignment]

    if isinstance(ascending, (tuple, list)):
        ascending = ascending[0]

    indexer = nargsort(
        k, kind=kind, ascending=ascending, na_position=na_position, key=key
    )
else:
    if inplace:
        exit(self._update_inplace(self))
    else:
        exit(self.copy(deep=None))

if is_range_indexer(indexer, len(indexer)):
    if inplace:
        exit(self._update_inplace(self))
    else:
        exit(self.copy(deep=None))

new_data = self._mgr.take(
    indexer, axis=self._get_block_manager_axis(axis), verify=False
)

if ignore_index:
    new_data.set_axis(
        self._get_block_manager_axis(axis), default_index(len(indexer))
    )

result = self._constructor(new_data)
if inplace:
    exit(self._update_inplace(result))
else:
    exit(result.__finalize__(self, method="sort_values"))
