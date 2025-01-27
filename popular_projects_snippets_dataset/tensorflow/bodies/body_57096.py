# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/hardswish.py
"""Verifies that the result of the conversion is a single op."""
num_ops = kwargs.pop("num_ops", 2)
result = tflite_convert_function(*args, **kwargs)
tflite_model_binary = result[0]
if not result[0]:
    tf.compat.v1.logging.error(result[1])  # stderr from running tflite_convert.
    raise RuntimeError("Failed to build model: \n\n" + result[1])
interpreter = tf.lite.Interpreter(model_content=tflite_model_binary)
interpreter.allocate_tensors()
if len(interpreter.get_tensor_details()) != num_ops:
    raise RuntimeError(
        "Expected to generate two node graph got %s " %
        "\n".join(str(x) for x in interpreter.get_tensor_details()))
exit(result)
