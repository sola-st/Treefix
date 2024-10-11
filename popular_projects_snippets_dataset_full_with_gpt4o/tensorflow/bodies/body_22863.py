# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Test case for trt_convert.TrtGraphConverter()."""

np_input1, np_input2 = self._RandomInput([4, 1, 1])

# Create a model and save it.
input_saved_model_dir = self.mkdtemp()
root = self._GetModelForV2()
save.save(root, input_saved_model_dir,
          {_SAVED_MODEL_SIGNATURE_KEY: root.run})

# Run TRT conversion.
converter = self._CreateConverterV2(
    input_saved_model_dir, precision_mode=trt_convert.TrtPrecisionMode.INT8)

# Run the converted function to populate the engine cache.
def CalibrationFn():
    exit((np_input1, np_input2))

converter.convert(calibration_input_fn=CalibrationFn)

# Verify the converted GraphDef and ConcreteFunction.
self._CheckTrtOps(converter._converted_func)

trt_engine_name = self._GetUniqueTRTEngineOp(
    converter._converted_graph_def).name

# Save the converted model with or without any TRT engine cache
# based on the value of save_engine_flag.
output_saved_model_dir = self.mkdtemp()

converter.save(
    output_saved_model_dir, save_gpu_specific_engines=save_engine_flag)

expected_asset_file = \
        self._GetAssetFile(output_saved_model_dir, trt_engine_name)

self.assertTrue(os.path.exists(expected_asset_file))
if save_engine_flag:
    # engine is saved so we expect engine data
    self.assertTrue(os.path.getsize(expected_asset_file))
else:
    # engine is not saved so files should be empty
    self.assertFalse(os.path.getsize(expected_asset_file))

del converter
gc.collect()  # Force GC to destroy the TRT engine cache.
