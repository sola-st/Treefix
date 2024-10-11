# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_flex_test.py
new_graph, inputs, outputs = self._createGraphWithCustomOp(
    opname='CustomAdd4')

# Import to load the custom opdef.
saved_model_dir = os.path.join(self.get_temp_dir(), 'model')
with ops.Graph().as_default():
    with session.Session() as sess:
        import_graph_def(new_graph, name='')
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)

converter = lite.TFLiteConverterV2.from_saved_model(saved_model_dir)
converter.target_spec.supported_ops = set([lite.OpsSet.SELECT_TF_OPS])
converter.target_spec.experimental_select_user_tf_ops = ['CustomAdd4']
tflite_model = converter.convert()

self.assertIn('FlexCustomAdd4', tflite_test_util.get_ops_list(tflite_model))
