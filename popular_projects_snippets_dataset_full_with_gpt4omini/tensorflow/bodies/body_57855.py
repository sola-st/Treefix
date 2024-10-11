# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test preserving AssertOp in a TF Lite model."""
saved_model_dir = os.path.join(self.get_temp_dir(), 'simple_savedmodel')
with tf.Graph().as_default():
    with tf.compat.v1.Session() as sess:
        in_tensor = tf.compat.v1.placeholder(
            shape=[10, 10], dtype=tf.float32, name='input')
        constant = tf.constant(value=1, dtype=tf.float32, shape=[10, 10])
        assert_op = tf.Assert(tf.less_equal(in_tensor, constant), [in_tensor])
        with tf.control_dependencies([assert_op]):
            out_tensor = in_tensor + constant
        inputs = {'x': in_tensor}
        outputs = {'y': out_tensor}
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)

    # Convert model and ensure model is not None.
converter = lite.TFLiteConverterV2.from_saved_model(saved_model_dir)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS
]
converter._experimental_preserve_assert_op = True
tflite_model = converter.convert()
self.assertTrue(tflite_model)

model = util._convert_model_from_bytearray_to_object(tflite_model)
has_assert = False
for op_code in model.operatorCodes:
    if op_code.customCode == b'FlexAssert':
        has_assert = True
        break
self.assertTrue(has_assert)
