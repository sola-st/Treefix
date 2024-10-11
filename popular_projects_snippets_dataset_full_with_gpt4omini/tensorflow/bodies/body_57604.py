# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
message = (
    'If input_tensors and output_tensors are None, both '
    'input_arrays_with_shape and output_arrays|control_output_arrays must '
    'be defined.')

# `output_arrays` is not defined.
with self.assertRaises(ValueError) as error:
    lite.TFLiteConverter(
        None, None, [], input_arrays_with_shape=[('input', [3,
                                                            9])]).convert()
self.assertEqual(message, str(error.exception))

# `input_arrays_with_shape` is not defined.
with self.assertRaises(ValueError) as error:
    lite.TFLiteConverter(None, [], None, output_arrays=['output']).convert()
self.assertEqual(message, str(error.exception))
