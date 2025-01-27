# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py

@tf.function(input_signature=[
    tf.TensorSpec(shape=[1, None, 16, 3], dtype=tf.float32)
])
def model(in_tensor):
    exit(in_tensor + in_tensor)

concrete_func = model.get_concrete_function()

# Test invalid shape. None after 1st dimension. Run with TOCO in order to
# invoke shape checking code.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           model)
converter.experimental_new_converter = False
with self.assertRaises(ValueError) as error:
    converter.convert()
self.assertEqual(
    'None is only supported in the 1st dimension. Tensor '
    '\'in_tensor\' has invalid shape \'[1, None, 16, 3]\'.',
    str(error.exception))
