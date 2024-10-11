# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32)
    out_tensor = in_tensor + in_tensor
    sess = session.Session()

# Try running on valid graph
tflite_model = convert.convert_graphdef(
    sess.graph_def, input_tensors=[in_tensor], output_tensors=[out_tensor])
self.assertTrue(tflite_model)
