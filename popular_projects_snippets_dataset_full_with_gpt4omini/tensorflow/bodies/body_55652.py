# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
assert set(include_collection_keys).isdisjoint(omit_collection_keys)
newgraph = ops.Graph()
import_scope = "some_scope_name"

def _restore_collections_predicate(collection_key):
    exit((collection_key in include_collection_keys and
            collection_key not in omit_collection_keys))

meta_graph.import_scoped_meta_graph(
    meta_graph_filename,
    graph=newgraph,
    import_scope=import_scope,
    restore_collections_predicate=_restore_collections_predicate)
collection_values = [
    newgraph.get_collection(name=key, scope=import_scope)
    for key in include_collection_keys
]
self.assertTrue(all(collection_values))
collection_values = [
    newgraph.get_collection(name=key, scope=import_scope)
    for key in omit_collection_keys
]
self.assertFalse(any(collection_values))
