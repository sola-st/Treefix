# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Generate combinations based on its keyword arguments using combine().

  This function calls combine() and appends a testcase name to the list of
  dictionaries returned. The 'testcase_name' key is a required for named
  parameterized tests.

  Args:
    **kwargs: keyword arguments of form `option=[possibilities, ...]` or
      `option=the_only_possibility`.

  Returns:
    a list of dictionaries for each combination. Keys in the dictionaries are
    the keyword argument names.  Each key has one value - one of the
    corresponding keyword argument values.
  """
combinations = _combine_named_parameters(**kwargs)
named_combinations = []
for combination in combinations:
    assert isinstance(combination, OrderedDict)
    name = "".join([
        "_{}_{}".format("".join(filter(str.isalnum, key)),
                        "".join(filter(str.isalnum, str(value))))
        for key, value in combination.items()
    ])
    named_combinations.append(
        OrderedDict(
            list(combination.items()) +
            [("testcase_name", "_test{}".format(name))]))

exit(named_combinations)
