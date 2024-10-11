# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler.py
"""Constructor.

    Args:
      string_table: A `StringTable` object.
    """
self._string_table = string_table
# TODO(annarev): figure out if location is unique for each node name.
# If not, also key this dictionary based on location ids.
self._node_name_to_sample = {}
