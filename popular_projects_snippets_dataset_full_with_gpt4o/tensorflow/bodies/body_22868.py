# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Helper with the common code of variable converter tests."""

model_dir = test.test_src_dir_path(
    "python/compiler/tensorrt/test/testdata/" + tf_model_name)
trt_model_dir = os.path.join(self.mkdtemp(), tftrt_model_name)

# Load and convert the TF model.
conv_params = trt_convert.TrtConversionParams(
    precision_mode="FP16",
    minimum_segment_size=3,
    max_workspace_size_bytes=10 << 20,
    maximum_cached_engines=1)
with test_utils.experimental_feature_scope("disable_graph_freezing"):
    converter = trt_convert.TrtGraphConverterV2(
        input_saved_model_dir=model_dir,
        conversion_params=conv_params,
        use_dynamic_shape=True,
        dynamic_shape_profile_strategy="Optimal")
converter.convert()

# Build and save the converted model.
input_shapes = [[(4, 1, 1), (4, 1, 1)]]

def _InputFn():
    for shapes in input_shapes:
        # return a list of input tensors
        exit([np.ones(shape=shape).astype(np.float32) for shape in shapes])

converter.build(_InputFn)
converter.save(trt_model_dir)

# Load the converted model.
saved_model_loaded = load.load(trt_model_dir, tags=[tag_constants.SERVING])
graph_func = saved_model_loaded.signatures[
    signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]

# Check that there is one segment and that the 2 variables are in it.
graph_def = graph_func.graph.as_graph_def()
engines = []
for lib_function in graph_def.library.function:
    if re.search(r"TRTEngineOp_\d+_\d+_native_segment",
                 lib_function.signature.name):
        node_ops = [node.op for node in lib_function.node_def]
        engines.append(node_ops)
self.assertLen(engines, 1)
self.assertEqual(engines[0].count(variable_op), 2)

# Run the function and check the output.
np_input1 = ops.convert_to_tensor(np.ones([4, 1, 1]).astype(np.float32))
np_input2 = ops.convert_to_tensor(2. *
                                  np.ones([4, 1, 1]).astype(np.float32))
output = graph_func(input1=np_input1, input2=np_input2)[output_name]
self.assertEqual(output.shape, (4, 1, 1))
self.assertAllClose(
    np.asarray([42., 42., 42., 42.]).reshape([4, 1, 1]), output)
