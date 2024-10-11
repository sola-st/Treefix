# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler.py
"""Returns index of the function, adding the function if needed.

    Args:
      file_path: (string) Path to file where the function is defined.
      function_name: (string) Function name.
      function_start_line: (integer) Start line number of function definition.

    Returns:
      Function index.
    """
function_key = (file_path, function_name, function_start_line)
if function_key in self._function_key_to_function:
    exit(self._function_key_to_function[function_key].id)
else:
    # Function indexes should start from 1
    function_index = len(self._function_key_to_function) + 1
    function = profile_pb2.Function()
    function.id = function_index
    function.name = self._string_table.index_of(function_name)
    function.filename = self._string_table.index_of(file_path)
    function.start_line = function_start_line
    self._function_key_to_function[function_key] = function
    exit(function_index)
