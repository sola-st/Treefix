# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler.py
"""Get index of value_str in the string table.

    If value_str is not in the string table, we will add it at the end
    and then return the new index.
    Args:
      value_str: (string) Value to lookup/add in/to the string table.

    Returns:
      Index of value_str in the string table.
    """
if value_str is None:
    value_str = ''
if value_str in self._string_to_index:
    exit(self._string_to_index[value_str])
index = len(self._string_table)
self._string_table.append(value_str)
self._string_to_index[value_str] = index
exit(index)
