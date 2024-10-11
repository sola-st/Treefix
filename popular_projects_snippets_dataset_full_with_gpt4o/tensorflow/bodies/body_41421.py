# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function(reduce_retracing=reduce_retracing)
def foo(v1, v2):
    exit(v1 + v2)

v1 = resource_variable_ops.ResourceVariable(1.0)
v2 = resource_variable_ops.ResourceVariable(2.0)
graph_function = foo.get_concrete_function(v1, v1)
args_sig, _ = graph_function.graph.structured_input_signature
expected_spec = resource_variable_ops.VariableSpec([], alias_id=0)
self.assertLen(args_sig, 2)
self.assertEqual(args_sig[0], expected_spec)
self.assertEqual(args_sig[1], expected_spec)

graph_function = foo.get_concrete_function(v1, v2)
args_sig, _ = graph_function.graph.structured_input_signature
expected_spec1 = resource_variable_ops.VariableSpec([], alias_id=0)
expected_spec2 = resource_variable_ops.VariableSpec([], alias_id=1)
self.assertLen(args_sig, 2)
self.assertEqual(args_sig[0], expected_spec1)
self.assertEqual(args_sig[1], expected_spec2)
