# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Load and execute a model that was saved in TF2.0."""

model_dir = test.test_src_dir_path(
    "python/compiler/tensorrt/test/testdata/tftrt_2.0_saved_model")
saved_model_loaded = load.load(model_dir, tags=[tag_constants.SERVING])
graph_func = saved_model_loaded.signatures[
    signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]

np_input1 = ops.convert_to_tensor(np.ones([4, 1, 1]).astype(np.float32))
np_input2 = ops.convert_to_tensor(np.ones([4, 1, 1]).astype(np.float32))
output = graph_func(input1=np_input1, input2=np_input2)["output_0"]

self.assertEqual(output.shape, (4, 1, 1))
self.assertAllClose(
    np.asarray([5.0, 5.0, 5.0, 5.0]).reshape([4, 1, 1]), output)
