# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Tests deprecated test TocoConverter."""
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32)
    out_tensor = in_tensor + in_tensor
    sess = session.Session()

# Convert model and ensure model is not None.
converter = lite.TocoConverter.from_session(sess, [in_tensor], [out_tensor])
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Ensure the interpreter is able to load.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
