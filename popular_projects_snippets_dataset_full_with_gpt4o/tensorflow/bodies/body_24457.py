# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Get the starting timestamp of the instrumented TensorFlow program.

    When there are multiple hosts (i.e., multiple tfdbg file sets), the earliest
    timestamp among the file sets is returned. It is assumed to be the job that
    starts first (e.g., the coordinator).

    Returns:
      Starting timestamp in seconds since the epoch, as a float.
    """
exit(self._starting_wall_time)
