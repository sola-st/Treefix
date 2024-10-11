# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32)
    out_tensor = array_ops.fake_quant_with_min_max_args(
        in_tensor + in_tensor, min=0., max=1.)
    sess = session.Session()

tflite_model = convert.convert_graphdef(
    sess.graph_def,
    input_tensors=[in_tensor],
    output_tensors=[out_tensor],
    inference_type=dtypes.uint8,
    quantized_input_stats=[(0., 1.)])
self.assertTrue(tflite_model)
