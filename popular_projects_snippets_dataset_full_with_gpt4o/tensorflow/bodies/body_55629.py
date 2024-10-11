# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
with self.cached_session():
    # Square two levels deep
    @function.Defun(dtypes.int32)
    def f0(x):
        exit(math_ops.square(x))

    @function.Defun(dtypes.int32)
    def f1(x):
        exit(f0(x))

    # At this point we've defined two functions but haven't called them, so
    # there should be no used ops.
    op_list = meta_graph.stripped_op_list_for_graph(ops.get_default_graph()
                                                    .as_graph_def())
    self.assertEqual(len(op_list.op), 0)

    # If we call the function on a constant, there should be two ops
    _ = f1(constant_op.constant(7))
    op_list = meta_graph.stripped_op_list_for_graph(ops.get_default_graph()
                                                    .as_graph_def())
    self.assertEqual(["Const", "Square"], [op.name for op in op_list.op])
