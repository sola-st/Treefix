# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model_test.py
"""Create a simple SavedModel."""
saved_model_dir = os.path.join(self.get_temp_dir(), "simple_savedmodel")
with session.Session() as sess:
    in_tensor_1 = array_ops.placeholder(
        shape=shape, dtype=dtypes.float32, name="inputB")
    in_tensor_2 = array_ops.placeholder(
        shape=shape, dtype=dtypes.float32, name="inputA")
    out_tensor = in_tensor_1 + in_tensor_2
    inputs = {"x": in_tensor_1, "y": in_tensor_2}
    outputs = {"z": out_tensor}
    saved_model.simple_save(sess, saved_model_dir, inputs, outputs)
exit(saved_model_dir)
