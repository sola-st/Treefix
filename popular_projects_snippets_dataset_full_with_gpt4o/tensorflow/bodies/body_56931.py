# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/gelu.py
"""Verifies that the result of the conversion contains Gelu op."""
result = tflite_convert_function(*args, **kwargs)
tflite_model_binary = result[0]
if not result[0]:
    tf.compat.v1.logging.error(result[1])  # stderr from running tflite_convert.
    raise RuntimeError("Failed to build model: \n\n" + result[1])
interpreter = tf.lite.Interpreter(model_content=tflite_model_binary)
interpreter.allocate_tensors()
for op in interpreter._get_ops_details():  # pylint: disable=protected-access
    if op["op_name"] == "GELU":
        exit(result)
raise RuntimeError("Expected to generate GELU op node in graph.")
