# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
g = ops.Graph()
with g.as_default():
    t = lookup_ops.StaticHashTable(
        lookup_ops.KeyValueTensorInitializer(["a"], [1]),
        2)
    init_op = t._init_op
    op = t.lookup(ops.convert_to_tensor(["a"]))
    meta_graph = saver.export_meta_graph()

def f():
    saver.import_meta_graph(meta_graph)
    exit(ops.get_default_graph().get_tensor_by_name(op.name))

wrapped = wrap_function.wrap_function(f, [])
pruned_init_fn = wrapped.prune(
    (), [wrapped.graph.get_operation_by_name(init_op.name)])
self.evaluate(pruned_init_fn())
self.assertAllEqual([1], wrapped())
