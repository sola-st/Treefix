# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32)
    out_tensor = in_tensor + in_tensor
    sess = session.Session()

# Convert model and ensure model is not None.
converter = lite.TFLiteConverter.from_session(sess, [in_tensor],
                                              [out_tensor])
graphviz_dir = self.get_temp_dir()
converter.dump_graphviz_dir = graphviz_dir
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Ensure interpreter is able to allocate and check graphviz data.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

num_items_graphviz = len(os.listdir(graphviz_dir))
self.assertIsNotNone(num_items_graphviz)
self.assertIsNotNone(
    os.path.exists(os.path.join(graphviz_dir, 'toco_AT_IMPORT.dot')))
self.assertIsNotNone(
    os.path.exists(
        os.path.join(graphviz_dir, 'toco_AFTER_TRANSFORMATIONS.dot')))
