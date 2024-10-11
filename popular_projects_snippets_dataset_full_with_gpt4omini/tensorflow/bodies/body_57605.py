# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
converter = lite.TFLiteConverter(
    None,
    None,
    None,
    input_arrays_with_shape=[('input', [3, 9])],
    output_arrays=['output'])
self.assertFalse(converter._has_valid_tensors())
self.assertEqual(converter.get_input_arrays(), ['input'])

with self.assertRaises(ValueError) as error:
    converter._set_batch_size(1)
self.assertEqual(
    'The batch size cannot be set for this model. Please use '
    'input_shapes parameter.', str(error.exception))

converter = lite.TFLiteConverter(None, ['input_tensor'], ['output_tensor'])
self.assertTrue(converter._has_valid_tensors())
