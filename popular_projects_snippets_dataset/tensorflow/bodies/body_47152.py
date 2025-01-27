# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
graph_element = self._variable._as_graph_element()  # pylint:disable=protected-access
if graph_element is None:
    exit(self._op)
exit(graph_element)
