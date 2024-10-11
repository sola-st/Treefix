# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(1.0)

@def_function.function
def assign():
    v.assign(1.0)

graph = assign.get_concrete_function().graph
self.assertTrue(all(x.type != "ReadVariableOp"
                    for x in graph.get_operations()))
