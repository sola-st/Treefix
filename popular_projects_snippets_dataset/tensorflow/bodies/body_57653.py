# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
# This is a regression test for the case where shape of dynamic output
# tensors changes between invocations.
# See also https://github.com/tensorflow/tensorflow/issues/26549
with ops.Graph().as_default():
    input_tensor = array_ops.placeholder(shape=[1, 1], dtype=dtypes.float32)
    input2_tensor = array_ops.placeholder(shape=[1], dtype=dtypes.float32)

    # The bug is triggered only when dynamic tensor is intermediate. Putting
    # some other ops around it.
    neg = math_ops.negative(input2_tensor)
    padding = array_ops.placeholder(shape=[2, 2], dtype=dtypes.int32)
    output_tensor = array_ops.pad(input_tensor, padding) + neg

    sess = session.Session()

converter = lite.TFLiteConverter.from_session(
    sess, [input_tensor, padding, input2_tensor], [output_tensor])
tflite_model = converter.convert()

interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
interpreter.set_tensor(input_details[1]['index'],
                       np.array([[1, 1], [1, 1]], dtype=np.int32))
interpreter.invoke()

# Without the fix, invocation will fail when changing the shape of
# intermediate dynamic tensors.
interpreter.set_tensor(input_details[1]['index'],
                       np.array([[2, 2], [2, 2]], dtype=np.int32))
interpreter.invoke()
