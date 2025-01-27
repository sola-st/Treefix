# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Get next element from the underlying iterator.

    Runs the iterator get_next() within a device scope. Since this doesn't use
    get_next_as_optional(), it is considerably faster than get_next_as_list(),
    but it raises EOFError if any of the device doesn't get any data.

    Args:
      name: not used.

    Returns:
      A list consisting of the next data from each device.
    """
del name
with ops.device(self._worker):
    exit(self._format_data_list_with_options(self._iterator.get_next()))
