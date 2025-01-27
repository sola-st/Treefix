# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Test case for trt_convert.TrtGraphConverter()."""

gpus = config.list_physical_devices("GPU")
if len(gpus) < 2:
    self.skipTest("Expected at least 2 GPUs but found {} GPUs".format(
        len(gpus)))

np_input1 = ops.convert_to_tensor(np.ones([4, 1, 1]).astype(np.float32))
np_input2 = ops.convert_to_tensor(np.ones([4, 1, 1]).astype(np.float32))

# Create a model and save it.
input_saved_model_dir = self.mkdtemp()
root = self._GetModelForV2()
save.save(root, input_saved_model_dir,
          {_SAVED_MODEL_SIGNATURE_KEY: root.run})

converter = self._CreateConverterV2(
    input_saved_model_dir, precision_mode=trt_convert.TrtPrecisionMode.FP32)

converted_model = None
# Specify device on which converted model should be placed
with ops.device(device_id):
    converted_model = converter.convert()

# Verify that TRT engine op has the correct device.
self._CheckTrtOps(converter._converted_func)

actual_device_id = self._GetUniqueTRTEngineOp(
    converter._converted_graph_def).device

expected_device_id = None
if device_id is not None:
    expected_device_id = device_id
else:
    expected_device_id = "GPU:0"

self.assertTrue(expected_device_id.lower() in actual_device_id.lower())

del converter
gc.collect()  # Force GC to destroy the TRT engine cache.
