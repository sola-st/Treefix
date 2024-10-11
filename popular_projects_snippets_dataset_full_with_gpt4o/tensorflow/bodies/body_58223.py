# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py

def create_graph_with_custom_add(opname='CustomAdd'):
    custom_opdefs_str = (
        'name: \'' + opname +
        '\' input_arg: {name: \'Input1\' type: DT_FLOAT} '
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

    exit((new_graph, inputs, outputs))

new_graph, inputs, outputs = create_graph_with_custom_add()

# Import to load the custom opdef.
saved_model_dir = os.path.join(self.get_temp_dir(), 'model')
with ops.Graph().as_default():
    with session.Session() as sess:
        import_graph_def(new_graph, name='')
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)

converter = lite.TFLiteConverterV2.from_saved_model(saved_model_dir)
self.convert_and_check_location_info(
    converter,
    converter_error_data_pb2.ConverterErrorData.NAMELOC,
    expected_sources='add')
exported_error = metrics._gauge_conversion_errors.get_cell(
    'CONVERT_TF_TO_TFLITE_MODEL', 'CONVERT_SAVED_MODEL', 'tf.CustomAdd',
    'ERROR_NEEDS_CUSTOM_OPS').value()
self.assertEqual(
    exported_error,
    "\'tf.CustomAdd\' op is neither a custom op nor a flex op\n"
    'Error code: ERROR_NEEDS_CUSTOM_OPS')
