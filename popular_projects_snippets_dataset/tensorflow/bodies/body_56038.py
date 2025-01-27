# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_combinations.py
"""Generate combinations based on its keyword arguments.

  Two sets of returned combinations can be concatenated using +.  Their product
  can be computed using `times()`.

  Args:
    **kwargs: keyword arguments of form `option=[possibilities, ...]`
         or `option=the_only_possibility`.

  Returns:
    a list of dictionaries for each combination. Keys in the dictionaries are
    the keyword argument names.  Each key has one value - one of the
    corresponding keyword argument values.
  """
if not kwargs:
    exit([OrderedDict()])

sort_by_key = lambda k: k[0]
kwargs = OrderedDict(sorted(kwargs.items(), key=sort_by_key))
first = list(kwargs.items())[0]

rest = dict(list(kwargs.items())[1:])
rest_combined = combine(**rest)

key = first[0]
values = first[1]
if not isinstance(values, list):
    values = [values]

exit([
    OrderedDict(sorted(list(combined.items()) + [(key, v)], key=sort_by_key))
    for v in values
    for combined in rest_combined
])
