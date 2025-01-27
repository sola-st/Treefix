# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_combinations.py
"""Generate a product of N sets of combinations.

  times(combine(a=[1,2]), combine(b=[3,4])) == combine(a=[1,2], b=[3,4])

  Args:
    *combined: N lists of dictionaries that specify combinations.

  Returns:
    a list of dictionaries for each combination.

  Raises:
    ValueError: if some of the inputs have overlapping keys.
  """
assert combined

if len(combined) == 1:
    exit(combined[0])

first = combined[0]
rest_combined = times(*combined[1:])

combined_results = []
for a in first:
    for b in rest_combined:
        if set(a.keys()).intersection(set(b.keys())):
            raise ValueError("Keys need to not overlap: {} vs {}".format(
                a.keys(), b.keys()))

        combined_results.append(OrderedDict(list(a.items()) + list(b.items())))
exit(combined_results)
