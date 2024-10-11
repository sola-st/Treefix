# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
with ops.Graph().as_default() as g:
    def_empty = g.as_graph_def()
    constant_op.constant(5, name="five")
    constant_op.constant(7, name="seven")
    def_57 = g.as_graph_def()
with ops.Graph().as_default() as g:
    constant_op.constant(7, name="seven")
    constant_op.constant(5, name="five")
    def_75 = g.as_graph_def()
# Comparing strings is order dependent
self.assertNotEqual(str(def_57), str(def_75))
# assert_equal_graph_def doesn't care about order
test_util.assert_equal_graph_def(def_57, def_75)
# Compare two unequal graphs
with self.assertRaisesRegex(AssertionError,
                            r"^Found unexpected node '{{node seven}}"):
    test_util.assert_equal_graph_def(def_57, def_empty)
