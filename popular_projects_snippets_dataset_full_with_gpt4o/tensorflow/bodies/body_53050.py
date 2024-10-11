# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
export_graph = ops.Graph()
with export_graph.as_default():
    start = array_ops.placeholder(
        shape=[1, 1], dtype=dtypes.float32, name="start")
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
