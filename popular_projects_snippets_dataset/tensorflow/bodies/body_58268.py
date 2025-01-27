# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_flex_test.py
# Create a graph that has one L2Loss op.
with ops.Graph().as_default():
    with session.Session() as sess:
        in_tensor = array_ops.placeholder(
            shape=[4], dtype=dtypes.float32, name='input')
        out_tensor = nn_ops.l2_loss(in_tensor)
        converter = lite.TFLiteConverter.from_session(sess, [in_tensor],
                                                      [out_tensor])
        converter.target_spec.supported_ops = set([lite.OpsSet.SELECT_TF_OPS])
        converter._experimental_allow_all_select_tf_ops = True
        tflite_model = converter.convert()
self.assertTrue(tflite_model)
self.assertIn('FlexL2Loss', tflite_test_util.get_ops_list(tflite_model))
