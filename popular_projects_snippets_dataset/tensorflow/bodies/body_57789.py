# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root = self._getSimpleVariableModel()
with self.assertRaises(ValueError) as error:
    _ = lite.TFLiteConverterV2.from_concrete_functions([root.f], root)
self.assertIn('call get_concrete_function', str(error.exception))
