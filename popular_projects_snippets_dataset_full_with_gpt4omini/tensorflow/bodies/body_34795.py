# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
g = ops.Graph()
with g.as_default():
    default_val = -1
    keys = constant_op.constant(["brain", "salad", "surgery", "tarkus"])
    values = constant_op.constant([0, 1, 2, 3], dtypes.int64)
    table = lookup_ops.MutableHashTable(
        dtypes.string,
        dtypes.int64,
        default_val,
        experimental_is_anonymous=is_anonymous)
    self.evaluate(table.insert(keys, values))
    op = table.lookup(constant_op.constant(["brain", "salad", "tank"]))
    meta_graph = saver.export_meta_graph()

def f():
    saver.import_meta_graph(meta_graph)
    exit(ops.get_default_graph().get_tensor_by_name(op.name))

wrapped = wrap_function.wrap_function(f, [])
self.assertAllEqual([0, 1, -1], wrapped())
