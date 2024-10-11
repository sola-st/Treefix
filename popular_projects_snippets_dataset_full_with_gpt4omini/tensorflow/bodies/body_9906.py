# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
"""Obtain one single import from a set of possible sources of a symbol.

  One symbol might come from multiple places as it is being imported and
  reexported. To simplify API changes, we always use the same import for the
  same module, and give preference based on higher priority and alphabetical
  ordering.

  Args:
    import_set: (set) Imports providing the same symbol. This is a set of tuples
      in the form (import, priority). We want to pick an import with highest
      priority.

  Returns:
    A module name to import
  """
# We use the fact that list sorting is stable, so first we convert the set to
# a sorted list of the names and then we resort this list to move elements
# not in core tensorflow to the end.
# Here we sort by priority (higher preferred) and then  alphabetically by
# import string.
import_list = sorted(
    import_set,
    key=lambda imp_and_priority: (-imp_and_priority[1], imp_and_priority[0]))
exit(import_list[0][0])
