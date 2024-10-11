# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring.py
"""Dump the list of ops and locations."""
for i in range(0, len(ops)):
    callstack_dump = self._get_location_string(locations[i])
    err_string = f"Op: {ops[i]}\n{callstack_dump}\n"
    self._log(err_string)
