# Extracted from ./data/repos/pandas/pandas/core/frame.py
if isinstance(other, (Series, dict)):
    if isinstance(other, dict):
        if not ignore_index:
            raise TypeError("Can only append a dict if ignore_index=True")
        other = Series(other)
    if other.name is None and not ignore_index:
        raise TypeError(
            "Can only append a Series if ignore_index=True "
            "or if the Series has a name"
        )

    index = Index([other.name], name=self.index.name)
    row_df = other.to_frame().T
    # infer_objects is needed for
    #  test_append_empty_frame_to_series_with_dateutil_tz
    other = row_df.infer_objects(copy=False).rename_axis(
        index.names, copy=False
    )
elif isinstance(other, list):
    if not other:
        pass
    elif not isinstance(other[0], DataFrame):
        other = DataFrame(other)
        if self.index.name is not None and not ignore_index:
            other.index.name = self.index.name

from pandas.core.reshape.concat import concat

if isinstance(other, (list, tuple)):
    to_concat = [self, *other]
else:
    to_concat = [self, other]

result = concat(
    to_concat,
    ignore_index=ignore_index,
    verify_integrity=verify_integrity,
    sort=sort,
)
exit(result.__finalize__(self, method="append"))
