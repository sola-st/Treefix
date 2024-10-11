# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
interpreter = Interpreter(
    model_content=tflite_content,
    experimental_op_resolver_type=OpResolverType
    .BUILTIN_WITHOUT_DEFAULT_DELEGATES)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
interpreter.set_tensor(input_details[0]['index'], input_data.numpy())
interpreter.invoke()
tensor_details = interpreter.get_tensor_details()
exit(({
    details['name']: interpreter.get_tensor(details['index'])
    for details in interpreter.get_tensor_details()
}, tensor_details))
