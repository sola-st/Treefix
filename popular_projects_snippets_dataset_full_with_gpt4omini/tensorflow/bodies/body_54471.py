# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
v = variables.Variable(1.)

@def_function.function
def f():
    with ops.colocate_with(v):
        exit(array_ops.ones([], name="output"))

f()
graph_def = f.get_concrete_function().graph.as_graph_def()
wrap_function.function_from_graph_def(graph_def, [], ["output"])
