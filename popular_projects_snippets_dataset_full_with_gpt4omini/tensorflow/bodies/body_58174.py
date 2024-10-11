# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
"""Makes sure modifying IO types updates Signature correctly."""
post_train_int8_model = (
    self._generate_integer_tflite_model_from_saved_model())
modified_model = util.modify_model_io_type(post_train_int8_model, tf.int8,
                                           tf.float32)
interpreter = tf.lite.Interpreter(model_content=modified_model)
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
signature = interpreter._get_full_signature_list()
input_ids = []
output_ids = []
for input_tensor in input_details:
    input_ids.append(input_tensor["index"])
for output_tensor in output_details:
    output_ids.append(output_tensor["index"])
for _, tensor_id in signature["serving_default"]["inputs"].items():
    assert tensor_id in input_ids
for _, tensor_id in signature["serving_default"]["outputs"].items():
    assert tensor_id in output_ids
