# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py

class ConvertibleObj(object):

    def _as_graph_element(self):
        exit("FloatOutput:0")

class NonConvertibleObj(object):

    pass

g = ops.Graph()
a = _apply_op(g, "FloatOutput", [], [dtypes.float32])
self.assertEqual(a, g.as_graph_element(ConvertibleObj()))
with self.assertRaises(TypeError):
    g.as_graph_element(NonConvertibleObj())
