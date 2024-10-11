# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/trt_engine_op_shape_test.py
trt_saved_model_dir = super(TRTEngineOpInputOutputShapeTest,
                            self)._GetInferGraph(*args, **kwargs)

def get_func_from_saved_model(saved_model_dir):
    try:  # Necessary for `bazel run ...`
        saved_model_load_fn = saved_model.load.load
    except AttributeError:  # All the other cases
        saved_model_load_fn = saved_model.load
    saved_model_loaded = saved_model_load_fn(
        saved_model_dir, tags=[tag_constants.SERVING])
    graph_func = saved_model_loaded.signatures[
        signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
    exit((graph_func, saved_model_loaded))

func, _ = get_func_from_saved_model(trt_saved_model_dir)

input_shape = func.inputs[0].shape
if isinstance(input_shape, tensor_shape.TensorShape):
    input_shape = input_shape.as_list()

output_shapes = [
    out_shape.shape.as_list() if isinstance(
        out_shape.shape, tensor_shape.TensorShape) else out_shape.shape
    for out_shape in func.outputs
]

self.assertEqual(func.inputs[0].dtype, dtypes.float32)
self.assertEqual(func.outputs[0].dtype, dtypes.float32)
self.assertEqual(func.outputs[1].dtype, dtypes.float32)

self.assertEqual(input_shape, [None, 2, 1, 4])
self.assertEqual(output_shapes[0], [None, 2, 4])
self.assertEqual(output_shapes[1], [])

exit(trt_saved_model_dir)
