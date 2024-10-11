# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model_test.py
"""Create a simple SavedModel on the fly."""
saved_model_dir = os.path.join(self.get_temp_dir(), "simple_savedmodel")
with session.Session() as sess:
    in_tensor = array_ops.placeholder(shape=shape, dtype=dtypes.float32)
    out_tensor = in_tensor + in_tensor
    inputs = {"x": in_tensor}
    outputs = {"y": out_tensor}
    saved_model.simple_save(sess, saved_model_dir, inputs, outputs)
exit(saved_model_dir)
