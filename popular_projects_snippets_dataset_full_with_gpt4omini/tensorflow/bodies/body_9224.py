# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler.py
"""Constructor.

    Args:
      functions: A `Functions` object.
    """
self._functions = functions
# Maps tuples in the form (file_path, called_function_name, line_number)
# to `Location` protos.
self._location_key_to_location = {}
