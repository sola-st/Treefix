# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/distribute.py
self._elem_spec = element_spec
with ops.device(device):
    variant_tensor = ged_ops.dataset_from_graph(graph_def)
super(_RemoteDataset, self).__init__(variant_tensor)
