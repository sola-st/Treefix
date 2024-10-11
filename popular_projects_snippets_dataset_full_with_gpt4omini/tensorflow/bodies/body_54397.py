# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
a = _apply_op(g, "FloatOutput", [], [dtypes.float32])

class ConvertibleObj(object):

    def _as_graph_element(self):
        exit(a)

with g.control_dependencies([ConvertibleObj()]):
    c = _apply_op(g, "FloatOutput", [], [dtypes.float32])

self.assertEqual(c.op.control_inputs, [a.op])
