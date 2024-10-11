# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test unfolding large splat constant in a TF Lite model."""
saved_model_dir = os.path.join(self.get_temp_dir(), 'simple_savedmodel')
with tf.Graph().as_default():
    with tf.compat.v1.Session() as sess:
        in_tensor = tf.compat.v1.placeholder(
            shape=[1000, 1000], dtype=tf.float32, name='input')
        constant = tf.constant(value=1, dtype=tf.float32, shape=[1000, 1000])
        out_tensor = in_tensor + constant
        inputs = {'x': in_tensor}
        outputs = {'y': out_tensor}
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)

    # Convert model and ensure model is not None.
converter = lite.TFLiteConverterV2.from_saved_model(saved_model_dir)
converter._experimental_unfold_large_splat_constant = unfold_large_constant
tflite_model = converter.convert()
self.assertTrue(tflite_model)

model = util._convert_model_from_bytearray_to_object(tflite_model)
if unfold_large_constant:
    self.assertEqual(model.operatorCodes[0].builtinCode,
                     schema_fb.BuiltinOperator.FILL)
    self.assertEqual(model.operatorCodes[1].builtinCode,
                     schema_fb.BuiltinOperator.ADD)
else:
    self.assertEqual(model.operatorCodes[0].builtinCode,
                     schema_fb.BuiltinOperator.ADD)

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual('input:0', input_details[0]['name'])
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([1000, 1000], input_details[0]['shape'])
self.assertEqual((0., 0.), input_details[0]['quantization'])

output_details = interpreter.get_output_details()
self.assertEqual('add:0', output_details[0]['name'])
self.assertEqual(np.float32, output_details[0]['dtype'])
self.assertAllEqual([1000, 1000], output_details[0]['shape'])
self.assertEqual((0., 0.), output_details[0]['quantization'])

interpreter.set_tensor(input_details[0]['index'],
                       np.ones(shape=[1000, 1000], dtype=np.float32))
interpreter.invoke()
self.assertAllEqual(
    np.full(shape=[1000, 1000], fill_value=2.0, dtype=np.float32),
    interpreter.get_tensor(output_details[0]['index']))
