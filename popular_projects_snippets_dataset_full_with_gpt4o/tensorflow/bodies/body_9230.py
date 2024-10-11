# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler.py
"""Constructor.

    Args:
      graph: A `Graph` instance.
      run_metadata: A list of `RunMetadata` objects.
    """
self._graph = graph
self._run_metadata = run_metadata
self._string_table = StringTable()
self._functions = Functions(self._string_table)
self._locations = Locations(self._functions)
