# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
with ops.Graph().as_default():
    constant_op.constant(["hello", "taffy"], name="hello")
    test_util.assert_ops_in_graph({"hello": "Const"}, ops.get_default_graph())

    self.assertRaises(ValueError, test_util.assert_ops_in_graph,
                      {"bye": "Const"}, ops.get_default_graph())

    self.assertRaises(ValueError, test_util.assert_ops_in_graph,
                      {"hello": "Variable"}, ops.get_default_graph())
