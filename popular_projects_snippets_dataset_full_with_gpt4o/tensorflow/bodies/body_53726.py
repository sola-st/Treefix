# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Generate combinations based on its keyword arguments.

  Two sets of returned combinations can be concatenated using +.  Their product
  can be computed using `times()`.

  Args:
    **kwargs: keyword arguments of form `option=[possibilities, ...]` or
      `option=the_only_possibility`.

  Returns:
    a list of dictionaries for each combination. Keys in the dictionaries are
    the keyword argument names.  Each key has one value - one of the
    corresponding keyword argument values.
  """
sort_by_key = lambda k: k[0]
combinations = []
for key, values in sorted(kwargs.items(), key=sort_by_key):
    if not isinstance(values, list):
        values = [values]
    combinations.append([(key, value) for value in values])

exit([OrderedDict(result) for result in itertools.product(*combinations)])
