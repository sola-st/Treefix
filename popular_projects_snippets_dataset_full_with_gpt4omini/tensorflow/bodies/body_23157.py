# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/trt_engine_op_shape_test.py
try:  # Necessary for `bazel run ...`
    saved_model_load_fn = saved_model.load.load
except AttributeError:  # All the other cases
    saved_model_load_fn = saved_model.load
saved_model_loaded = saved_model_load_fn(
    saved_model_dir, tags=[tag_constants.SERVING])
graph_func = saved_model_loaded.signatures[
    signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
exit((graph_func, saved_model_loaded))
