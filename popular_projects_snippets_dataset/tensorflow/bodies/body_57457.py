# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
custom_opdefs_str = (
    'name: \'' + opname + '\' input_arg: {name: \'Input1\' type: DT_FLOAT} '
    'input_arg: {name: \'Input2\' type: DT_FLOAT} output_arg: {name: '
    '\'Output\' type: DT_FLOAT}')

# Create a graph that has one add op.
new_graph = graph_pb2.GraphDef()
with ops.Graph().as_default():
    with session.Session() as sess:
        in_tensor = array_ops.placeholder(
            shape=[1, 16, 16, 3], dtype=dtypes.float32, name='input')
        out_tensor = in_tensor + in_tensor
        inputs = {'x': in_tensor}
        outputs = {'z': out_tensor}

        new_graph.CopyFrom(sess.graph_def)

    # Rename Add op name to opname.
for node in new_graph.node:
    if node.op.startswith('Add'):
        node.op = opname
        del node.attr['T']

    # Register custom op defs to import modified graph def.
register_custom_opdefs([custom_opdefs_str])

# Store saved model.
saved_model_dir = self._getFilepath('model')
with ops.Graph().as_default():
    with session.Session() as sess:
        import_graph_def(new_graph, name='')
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)
exit((saved_model_dir, custom_opdefs_str))
