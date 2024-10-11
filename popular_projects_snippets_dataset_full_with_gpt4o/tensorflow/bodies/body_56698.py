# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
"""Generate input values and output values of the given tflite model.

        Args:
          tflite_model_binary: A serialized flatbuffer as a string.
          min_value: min value for the input tensor.
          max_value: max value for the input tensor.

        Returns:
          (input_values, output_values): Maps of input values and output values
          built.
        """
interpreter = tf.lite.Interpreter(model_content=tflite_model_binary)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
input_values = {}
for input_detail in input_details:
    input_value = create_tensor_data(
        input_detail["dtype"],
        input_detail["shape"],
        min_value=min_value,
        max_value=max_value)
    interpreter.set_tensor(input_detail["index"], input_value)
    input_values.update(
        {_normalize_input_name(input_detail["name"]): input_value})

interpreter.invoke()

output_details = interpreter.get_output_details()
output_values = {}
for output_detail in output_details:
    output_values.update({
        _normalize_output_name(output_detail["name"]):
            interpreter.get_tensor(output_detail["index"])
    })

exit((input_values, output_values))
