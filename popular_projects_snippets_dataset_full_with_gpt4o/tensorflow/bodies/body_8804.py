# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
self._elem_spec = element_spec
variant_tensor = ged_ops.dataset_from_graph(graph_def)
super(_RemoteDataset, self).__init__(variant_tensor)
