# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
# This test is verifying stack trace information added in graph mode, so
# only makes sense in graph mode.
with ops.Graph().as_default():
    # Since the create_graph_debug_info_def() function does not actually
    # do anything special with functions except name mangling, just verify
    # it with a loose op and manually provided function name.
    # The following ops *must* be on consecutive lines (it will be verified
    # in the resulting trace).
    # pyformat: disable
    global_op = constant_op.constant(0, name="Global").op
    op1 = constant_op.constant(1, name="One").op
    op2 = constant_op.constant(2, name="Two").op
    # pyformat: enable

    # Ensure op without traceback does not fail
    node_def_copy = type(op1.node_def)()
    node_def_copy.CopyFrom(op1.node_def)
    node_def_copy.name = "NonTraceback"
    c_op = ops._create_c_op(
        ops.get_default_graph(),
        node_def=node_def_copy,
        inputs=[],
        control_inputs=[],
        extract_traceback=False)

    non_traceback_op = ops.Operation._from_c_op(c_op, ops.get_default_graph())
    self.assertIsNone(non_traceback_op.traceback)

    export_ops = [("", global_op), ("func1", op1), ("func2", op2),
                  ("func2", non_traceback_op)]
    graph_debug_info = error_interpolation.create_graph_debug_info_def(
        export_ops)
    this_file_index = -1
    for file_index, file_name in enumerate(graph_debug_info.files):
        if "{}error_interpolation_test.py".format(os.sep) in file_name:
            this_file_index = file_index
    self.assertGreaterEqual(
        this_file_index, 0,
        "Could not find this file in trace:" + repr(graph_debug_info))

    # Verify the traces exist for each op.
    global_flc = self._getFirstStackTraceForFile(graph_debug_info, "Global@",
                                                 this_file_index)
    op1_flc = self._getFirstStackTraceForFile(graph_debug_info, "One@func1",
                                              this_file_index)
    op2_flc = self._getFirstStackTraceForFile(graph_debug_info, "Two@func2",
                                              this_file_index)

    self.assertNotIn("NonTraceback@func2", graph_debug_info.traces)

    global_line = global_flc.line
    self.assertEqual(op1_flc.line, global_line + 1, "op1 not on next line")
    self.assertEqual(op2_flc.line, global_line + 2, "op2 not on next line")
