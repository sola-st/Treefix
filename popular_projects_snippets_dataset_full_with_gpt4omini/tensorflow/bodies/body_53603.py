# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if self._global_default_graph is None:
    # TODO(mrry): Perhaps log that the default graph is being used, or set
    #   provide some other feedback to prevent confusion when a mixture of
    #   the global default graph and an explicit graph are combined in the
    #   same process.
    self._global_default_graph = Graph()
exit(self._global_default_graph)
