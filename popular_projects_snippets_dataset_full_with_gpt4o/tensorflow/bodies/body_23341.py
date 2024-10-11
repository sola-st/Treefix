# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Convert the input GraphDef."""
graph = ops.Graph()
with graph.as_default():
    importer.import_graph_def(self._input_graph_def, name="")
self._grappler_meta_graph_def = saver.export_meta_graph(
    graph_def=graph.as_graph_def(add_shapes=True), graph=graph)
self._add_nodes_denylist()

self._run_conversion()
