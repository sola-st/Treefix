# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py

def make_graph_with_partitioned_variables(use_resource):
    variable_scope.get_variable(
        name="weights",
        partitioner=partitioned_variables.fixed_size_partitioner(3, axis=0),
        initializer=random_ops.truncated_normal([100, 10]),
        use_resource=use_resource)
    # The next variable illustrates the necessity of restoring collections
    # in a deterministic fashion when using ResourceVariables.
    variable_scope.get_variable(
        name="another",
        shape=[],
        collections=["a", "b", "z", "f", "e", "d", "g"],
        use_resource=use_resource)

self._testExportImportAcrossScopes(
    make_graph_with_partitioned_variables, use_resource=False)
self._testExportImportAcrossScopes(
    make_graph_with_partitioned_variables, use_resource=True)
