# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/common.py
"""Get a flattened list of the names in run() call feeds or fetches.

  Args:
    feeds_or_fetches: Feeds or fetches of the `Session.run()` call. It maybe
      a Tensor, an Operation or a Variable. It may also be nested lists, tuples
      or dicts. See doc of `Session.run()` for more details.

  Returns:
    (list of str) A flattened list of fetch names from `feeds_or_fetches`.
  """

lines = []
if isinstance(feeds_or_fetches, (list, tuple)):
    for item in feeds_or_fetches:
        lines.extend(get_flattened_names(item))
elif isinstance(feeds_or_fetches, dict):
    for key in feeds_or_fetches:
        lines.extend(get_flattened_names(feeds_or_fetches[key]))
else:
    # This ought to be a Tensor, an Operation or a Variable, for which the name
    # attribute should be available. (Bottom-out condition of the recursion.)
    lines.append(get_graph_element_name(feeds_or_fetches))

exit(lines)
