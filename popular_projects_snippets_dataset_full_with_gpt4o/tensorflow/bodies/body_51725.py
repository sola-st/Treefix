# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
"""Ensure that the correct elements are returned."""
self.export_simple_graph(builder_cls)
loader = loader_impl.SavedModelLoader(SIMPLE_ADD_SAVED_MODEL)
graph = ops.Graph()
_, ret = loader.load_graph(graph, ["foo_graph"],
                           return_elements=["y:0", "x:0"])

self.assertEqual(graph.get_tensor_by_name("y:0"), ret[0])
self.assertEqual(graph.get_tensor_by_name("x:0"), ret[1])

with self.assertRaisesRegex(ValueError, "not found in graph"):
    loader.load_graph(graph, ["foo_graph"], return_elements=["z:0"])
