# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
graph_defs = []
num_graphs = 10
for _ in range(num_graphs):
    with ops_lib.Graph().as_default() as g:
        for i in range(20):
            resource_variable_ops.ResourceVariable(i, name="var%s" % i)
        saver_module.Saver()
        graph_defs.append(g.as_graph_def())
for i in range(num_graphs - 1):
    self.assertEqual(graph_defs[i], graph_defs[i + 1])
