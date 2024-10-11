# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Re-evaluate the obj with a groupby aggregation.
        """
grouper = self.grouper

if self._selected_obj.ndim == 1:
    obj = self._selected_obj
else:
    # Excludes `on` column when provided
    obj = self._obj_with_exclusions
grouped = get_groupby(
    obj, by=None, grouper=grouper, axis=self.axis, group_keys=self.group_keys
)

try:
    if isinstance(obj, ABCDataFrame) and callable(how):
        # Check if the function is reducing or not.
        result = grouped._aggregate_item_by_item(how, *args, **kwargs)
    else:
        result = grouped.aggregate(how, *args, **kwargs)
except DataError:
    # got TypeErrors on aggregation
    result = grouped.apply(how, *args, **kwargs)
except (AttributeError, KeyError):
    # we have a non-reducing function; try to evaluate
    # alternatively we want to evaluate only a column of the input

    # test_apply_to_one_column_of_df the function being applied references
    #  a DataFrame column, but aggregate_item_by_item operates column-wise
    #  on Series, raising AttributeError or KeyError
    #  (depending on whether the column lookup uses getattr/__getitem__)
    result = grouped.apply(how, *args, **kwargs)

except ValueError as err:
    if "Must produce aggregated value" in str(err):
        # raised in _aggregate_named
        # see test_apply_without_aggregation, test_apply_with_mutated_index
        pass
    else:
        raise

    # we have a non-reducing function
    # try to evaluate
    result = grouped.apply(how, *args, **kwargs)

exit(self._wrap_result(result))
