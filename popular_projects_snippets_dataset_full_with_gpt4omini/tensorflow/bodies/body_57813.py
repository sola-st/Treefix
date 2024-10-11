# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test converting SignatureDef is correct and uses SignatureDef API."""
root = self._getSimpleVariableModel()
input_data = tf.constant(1., shape=[1])
concrete_func = root.f.get_concrete_function(input_data)

converter = lite.TFLiteConverterV2.from_concrete_functions(
    [concrete_func], trackable_obj=autotrackable.AutoTrackable())
tflite_model = converter.convert()

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
signature_defs = interpreter.get_signature_list()
# Verify that there is no SignatureDef structure found.
self.assertEqual(len(signature_defs), 0)
