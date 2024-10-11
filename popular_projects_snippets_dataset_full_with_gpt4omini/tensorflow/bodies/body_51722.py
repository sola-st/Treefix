# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
self.export_simple_graph(builder_cls)
loader = loader_impl.SavedModelLoader(SIMPLE_ADD_SAVED_MODEL)
meta_graph = loader.get_meta_graph_def_from_tags(["foo_graph"])
self.assertIsNotNone(meta_graph)
self.assertIn("foo", meta_graph.signature_def)
self.assertIn("bar", meta_graph.signature_def)
