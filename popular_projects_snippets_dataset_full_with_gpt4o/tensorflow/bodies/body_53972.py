# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
def get_graph_def():
    with ops.Graph().as_default() as g:
        x = constant_op.constant([2, 9], name="x")
        keys = constant_op.constant([1, 2], name="keys")
        values = constant_op.constant([3, 4], name="values")
        default = constant_op.constant(-1, name="default")
        table = lookup_ops.StaticHashTable(
            lookup_ops.KeyValueTensorInitializer(keys, values), default)
        _ = table.lookup(x)
    exit(g.as_graph_def())
def_1 = get_graph_def()
def_2 = get_graph_def()
# The unique shared_name of each table makes the graph unequal.
with self.assertRaisesRegex(AssertionError, "hash_table_"):
    test_util.assert_equal_graph_def(def_1, def_2,
                                     hash_table_shared_name=False)
# That can be ignored. (NOTE: modifies GraphDefs in-place.)
test_util.assert_equal_graph_def(def_1, def_2,
                                 hash_table_shared_name=True)
