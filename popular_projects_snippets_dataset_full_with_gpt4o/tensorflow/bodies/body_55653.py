# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
meta_graph_filename = os.path.join(
    _TestDir("selected_collections_import"), "meta_graph.pb")

graph = ops.Graph()
# Add a variable to populate two collections. The functionality tested is
# not specific to variables, but using variables in the test is convenient.
with graph.as_default():
    variables.Variable(initial_value=1.0, trainable=True)
self.assertTrue(
    all(
        graph.get_collection(key)
        for key in
        [ops.GraphKeys.GLOBAL_VARIABLES, ops.GraphKeys.TRAINABLE_VARIABLES]
    ))
meta_graph.export_scoped_meta_graph(
    filename=meta_graph_filename, graph=graph)

def _test_import(include_collection_keys, omit_collection_keys):
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

_test_import(
    include_collection_keys=[
        ops.GraphKeys.GLOBAL_VARIABLES, ops.GraphKeys.TRAINABLE_VARIABLES
    ],
    omit_collection_keys=[])
_test_import(
    include_collection_keys=[ops.GraphKeys.GLOBAL_VARIABLES],
    omit_collection_keys=[ops.GraphKeys.TRAINABLE_VARIABLES])
_test_import(
    include_collection_keys=[ops.GraphKeys.TRAINABLE_VARIABLES],
    omit_collection_keys=[ops.GraphKeys.GLOBAL_VARIABLES])
_test_import(
    include_collection_keys=[],
    omit_collection_keys=[
        ops.GraphKeys.GLOBAL_VARIABLES, ops.GraphKeys.TRAINABLE_VARIABLES
    ])
