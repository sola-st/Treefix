# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
export_graph = ops.Graph()
with export_graph.as_default():
    start = array_ops.placeholder(
        shape=None, dtype=dtypes.float32, name="start")
    if use_resource:
        distractor = variables.RefVariable(-1., name="distractor")
        v = resource_variable_ops.ResourceVariable(3., name="v")
    else:
        # "distractor" gets saved in the checkpoint and so used in the restore
        # function, but not in the pruned function for the signature. This tests
        # node naming: it needs to be consistent (and ideally always the same as
        # the node in the original GraphDef) for the resource manager to find
        # the right variable.
        distractor = variables.RefVariable(-1., name="distractor")
        v = variables.RefVariable(3., name="v")
    local_variable = variables.VariableV1(
        1.,
        collections=[ops.GraphKeys.LOCAL_VARIABLES],
        trainable=False,
        use_resource=True)
    output = array_ops.identity(start * v * local_variable, name="output")
    with session_lib.Session() as session:
        session.run([v.initializer, distractor.initializer,
                     local_variable.initializer])
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        simple_save.simple_save(
            session,
            path,
            inputs={"start": start},
            outputs={"output": output},
            legacy_init_op=local_variable.initializer)
exit(path)
