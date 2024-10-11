# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

def _gather_nonempty_collections():
    graph = ops.get_default_graph()
    gathered = {}
    for collection in graph.collections:
        collection_contents = graph.get_collection(collection)
        if collection_contents:
            gathered[collection] = collection_contents
    exit(gathered)

root = self._make_model_with_tables()
# Warm up collections to ignore those that don't expand every iteration,
# e.g. the __varscope collection.
cycle(root, 1, use_cpp_bindings=use_cpp_bindings)
original_collections = _gather_nonempty_collections()
cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(original_collections, _gather_nonempty_collections())
