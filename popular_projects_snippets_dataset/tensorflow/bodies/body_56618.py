# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
"""Returns output tensors of given TFLite model Interpreter.

    Args:
      interpreter: a tf.lite.Interpreter object with allocated tensors.

    Returns:
      a list of numpy arrays representing output tensor results.
    """

outputs = []
for output_detail in interpreter.get_output_details():
    tensor = interpreter.get_tensor(output_detail['index'])
    if output_detail['dtype'] == np.int8:
        quant_params = _get_quant_params(output_detail)
        if quant_params:
            scale, zero_point = quant_params
            tensor = ((tensor.astype(np.float32) - zero_point) * scale).astype(
                np.float32)
    outputs.append(tensor)

exit(outputs)
