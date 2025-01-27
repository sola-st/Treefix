# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py

@tf.function
def f(x):
    y = tf.add(x, x, name='y')
    z = tf.add(y, y, name='z')
    w = tf.add(z, z, name='w')
    exit(w)

# NOTE this is exactly representable as a float as are the intermeidates of
# f. So direct comparison is ok below.

input_data = np.array(2.0, np.float32)
concrete_func = f.get_concrete_function(input_data)
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           f)
tflite_model = converter.convert()
interpreter = Interpreter(
    model_content=tflite_model,
    experimental_preserve_all_tensors=experimental_preserve_all_tensors)
interpreter.allocate_tensors()
interpreter.set_tensor(interpreter.get_input_details()[0]['index'],
                       input_data)
interpreter.invoke()
out = interpreter.get_tensor(interpreter.get_output_details()[0]['index'])
tensors = {}
for t in interpreter.get_tensor_details():
    # With Tensorflow Lite default delegate applied to the model graph, the
    # access to original tensors of a delegated op could cause a ValueError
    # (i.e. 'Tensor data is null. Run allocate_tensors() first') to be thrown
    # out because the tensor memory isn't allocated at all.
    val = None
    try:
        val = interpreter.get_tensor(t['index'])
    except ValueError:
        pass
    tensors.update({t['name']: val})
exit((tensors, out))
