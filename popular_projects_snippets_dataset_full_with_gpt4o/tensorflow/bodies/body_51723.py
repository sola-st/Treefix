# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
self.export_simple_graph(builder_cls)
loader = loader_impl.SavedModelLoader(SIMPLE_ADD_SAVED_MODEL)
with self.assertRaises(RuntimeError):
    loader.get_meta_graph_def_from_tags([])
with self.assertRaises(RuntimeError):
    loader.get_meta_graph_def_from_tags([""])
with self.assertRaises(RuntimeError):
    loader.get_meta_graph_def_from_tags(["not_a_graph"])
