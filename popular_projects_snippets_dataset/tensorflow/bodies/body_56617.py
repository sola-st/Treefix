# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
"""Sets input tensors into TFLite model Interpreter.

    Args:
      interpreter: a tf.lite.Interpreter object with allocated tensors.
      tensor_data: a list of Numpy array data.
      initialize: set to true when input is first set for the interpreter, to
        set input shapes and allocate tensors.

    Raises:
      ValueError: when inputs can't be set, or size of provided inputs does not
      match size of model inputs.
    """
input_details = interpreter.get_input_details()
if len(input_details) != len(tensor_data):
    raise ValueError(
        'Number of inputs provided ({}) does not match number of inputs to '
        'the model ({})'.format(len(tensor_data), len(input_details)))

if initialize:
    for input_detail, tensor in zip(input_details, tensor_data):
        interpreter.resize_tensor_input(input_detail['index'], tensor.shape)
    interpreter.allocate_tensors()

for input_detail, tensor in zip(input_details, tensor_data):
    if tensor.dtype == np.float32 and input_detail['dtype'] == np.int8:
        quant_params = _get_quant_params(input_detail)
        if quant_params:
            scale, zero_point = quant_params
            tensor = np.round((tensor / scale) + zero_point).astype(np.int8)
    interpreter.set_tensor(input_detail['index'], tensor)
