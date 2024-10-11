# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/lift_to_graph_test.py
v1 = resource_variable_ops.ResourceVariable(1.0)
v2 = resource_variable_ops.ResourceVariable(2.0)
v3 = resource_variable_ops.ResourceVariable(3.0)

@def_function.function
def fn():
    exit(v1 + v2 + v3)

concrete_fn = fn.get_concrete_function()
original_captures = concrete_fn.graph.internal_captures
outputs = concrete_fn.graph.outputs

for _ in range(100):
    g = func_graph.FuncGraph('lifted')

    lift_to_graph.lift_to_graph(
        outputs, g, add_sources=True, handle_captures=True)
    lifted_captures = g.internal_captures
    self.assertLen(lifted_captures, 3)
    for original, lifted in zip(original_captures, lifted_captures):
        self.assertEqual(original.name, lifted.name)
