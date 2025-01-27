# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
with self.cached_session():
    # Creates a graph.
    v0 = variables.VariableV1(0.0)
    var = variables.VariableV1(10.0)
    math_ops.add(v0, var)

    @function.Defun(dtypes.float32)
    def minus_one(x):
        exit(x - 1)

    minus_one(array_ops.identity(v0))
    save = saver_module.Saver({"v0": v0})
    variables.global_variables_initializer()

    # Generates MetaGraphDef.
    meta_graph_def = save.export_meta_graph()
    ops = [o.name for o in meta_graph_def.meta_info_def.stripped_op_list.op]
    if save._write_version is saver_pb2.SaverDef.V1:
        self.assertEqual(ops, [
            "AddV2", "Assign", "Const", "Identity", "NoOp",
            "PlaceholderWithDefault", "RestoreV2", "SaveSlices", "Sub",
            "VariableV2"
        ])
    else:
        self.assertEqual(ops, [
            "AddV2", "Assign", "Const", "Identity", "NoOp",
            "PlaceholderWithDefault", "RestoreV2", "SaveV2", "Sub", "VariableV2"
        ])

    # Test calling stripped_op_list_for_graph directly
    op_list = meta_graph.stripped_op_list_for_graph(meta_graph_def.graph_def)
    self.assertEqual(ops, [o.name for o in op_list.op])
    for o in op_list.op:
        self.assertEqual(o.summary, "")
        self.assertEqual(o.description, "")
