# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context_test.py

@def_function.function
def f(x):
    exit(x + constant_op.constant(1.))

with context.collect_graphs() as graphs:
    with ops.device('CPU:0'):
        f(constant_op.constant(1.))

self.assertLen(graphs, 1)
graph, = graphs
self.assertIn('CPU:0', graph.node[0].device)
