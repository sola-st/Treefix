# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
"""Tests export and importing a graph across scopes.

    Args:
      graph_fn: A closure that creates a graph on the current scope.
      use_resource: A bool indicating whether or not to use ResourceVariables.
    """
with ops.Graph().as_default() as original_graph:
    with variable_scope.variable_scope("dropA/dropB/keepA"):
        graph_fn(use_resource=use_resource)
exported_meta_graph_def = meta_graph.export_scoped_meta_graph(
    graph=original_graph,
    export_scope="dropA/dropB")[0]

with ops.Graph().as_default() as imported_graph:
    meta_graph.import_scoped_meta_graph(
        exported_meta_graph_def,
        import_scope="importA")

with ops.Graph().as_default() as expected_graph:
    with variable_scope.variable_scope("importA/keepA"):
        graph_fn(use_resource=use_resource)

result = meta_graph.export_scoped_meta_graph(graph=imported_graph)[0]
expected = meta_graph.export_scoped_meta_graph(graph=expected_graph)[0]

if use_resource:
    # Clear all shared_name attributes before comparing, since they are
    # orthogonal to scopes and are not updated on export/import.
    for meta_graph_def in [result, expected]:
        for node in meta_graph_def.graph_def.node:
            shared_name_attr = "shared_name"
            shared_name_value = node.attr.get(shared_name_attr, None)
            if shared_name_value and shared_name_value.HasField("s"):
                if shared_name_value.s:
                    node.attr[shared_name_attr].s = b""

test_util.assert_meta_graph_protos_equal(self, expected, result)
