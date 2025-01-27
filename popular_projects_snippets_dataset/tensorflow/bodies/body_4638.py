# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2.py
if ops.get_default_graph().finalized:
    exit(self._variables[0]._graph_element)
exit(self.read_value())
