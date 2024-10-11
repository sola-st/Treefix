# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
with ops.Graph().as_default():
    in_tensor_1 = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32, name="inputA")
    in_tensor_2 = array_ops.placeholder(
        shape=[1, 16, 16, 3], dtype=dtypes.float32, name="inputB")
    _ = array_ops.fake_quant_with_min_max_args(
        in_tensor_1 + in_tensor_2, min=0., max=1., name="output")
    sess = session.Session()

with self.assertRaises(ValueError) as error:
    convert.convert_graphdef_with_arrays(
        sess.graph_def,
        input_arrays_with_shape=[("inputA", [1, 16, 16, 3]),
                                 ("inputB", [1, 16, 16, 3])],
        output_arrays=["output"],
        control_output_arrays=None,
        inference_type=dtypes.uint8,
        enable_mlir_converter=False)
self.assertEqual(
    "The `quantized_input_stats` flag must be defined when either "
    "`inference_type` flag or `inference_input_type` flag is set to "
    "tf.int8 or tf.uint8.", str(error.exception))
