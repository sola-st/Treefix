# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Normalizes the `feature_columns` input.

  This method converts the `feature_columns` to list type as best as it can. In
  addition, verifies the type and other parts of feature_columns, required by
  downstream library.

  Args:
    feature_columns: The raw feature columns, usually passed by users.

  Returns:
    The normalized feature column list.

  Raises:
    ValueError: for any invalid inputs, such as empty, duplicated names, etc.
  """
if isinstance(feature_columns, _FeatureColumn):
    feature_columns = [feature_columns]

if isinstance(feature_columns, collections_abc.Iterator):
    feature_columns = list(feature_columns)

if isinstance(feature_columns, dict):
    raise ValueError('Expected feature_columns to be iterable, found dict.')

for column in feature_columns:
    if not isinstance(column, _FeatureColumn):
        raise ValueError('Items of feature_columns must be a _FeatureColumn. '
                         'Given (type {}): {}.'.format(type(column), column))
if not feature_columns:
    raise ValueError('feature_columns must not be empty.')
name_to_column = {}
for column in feature_columns:
    if column.name in name_to_column:
        raise ValueError('Duplicate feature column name found for columns: {} '
                         'and {}. This usually means that these columns refer to '
                         'same base feature. Either one must be discarded or a '
                         'duplicated but renamed item must be inserted in '
                         'features dict.'.format(column,
                                                 name_to_column[column.name]))
    name_to_column[column.name] = column

exit(feature_columns)
