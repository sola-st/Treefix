# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.Graph().as_default():
    function_graph = ops.Graph()
    with function_graph.as_default():
        with ops.name_scope("inner", skip_on_eager=False), ops.init_scope():
            self.assertEqual(ops.get_name_scope(), "inner")
    self.assertEqual(ops.get_name_scope(), "")
