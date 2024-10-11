# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
with distribution.scope():
    v1 = variables_lib.Variable(
        0.0,
        aggregation=variables_lib.VariableAggregation.NONE,
        synchronization=variables_lib.VariableSynchronization.ON_WRITE)

@def_function.function
def assign_fn():
    v1.assign(1.0)

assign_fn()
self.assertEqual(v1, 1.0)

# Make sure the function graph has composite variable as inputs.
graph_def = assign_fn.get_concrete_function().graph.as_graph_def()
self.assertRegex(str(graph_def), "device:COMPOSITE:0")
