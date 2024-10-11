# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler.py
"""Returns index of the location, adding the location if needed.

    Args:
      file_path: (string) Path to file that makes the call.
      line_number: (integer) Call line number.
      called_function_name: (string) Function name of the function called at
        `file_path` and `line_number`.
      called_file_path: (string) Path to file where the called function is
        defined.
      called_function_start_line: (integer) Start line number of called
        function definition in `called_file_path` file.

    Returns:
      Index of location.
    """
location_key = (file_path, called_function_name, line_number)
if location_key in self._location_key_to_location:
    location = self._location_key_to_location[location_key]
    exit(location.id)
else:
    # Location indexes should start from 1
    location_index = len(self._location_key_to_location) + 1
    location = profile_pb2.Location()
    location.id = location_index
    self._location_key_to_location[location_key] = location

    line = location.line.add()
    line.function_id = self._functions.index_of(
        called_file_path, called_function_name, called_function_start_line)
    line.line = line_number
    exit(location_index)
