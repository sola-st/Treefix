# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
self._graph_def = graph_def
self._tensor_data = {}
self._build_node_defs_list()
self._variable_names_allowlist = variable_names_allowlist
self._variable_names_denylist = variable_names_denylist
