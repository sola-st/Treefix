# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler.py
"""Constructor.

    Args:
      string_table: A `StringTable` object.
    """
self._string_table = string_table
# Maps tuples in the form (file_path, function_name, start_line_number)
# to `Function` protos.
self._function_key_to_function = {}
