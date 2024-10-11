# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
# Create a model and save it.
input_saved_model_dir = self.mkdtemp()
root = self._GetModelForV2()
if np_input is None:
    expected_output = None
else:
    expected_output = root.run(np_input[0], np_input[1])

save.save(root, input_saved_model_dir,
          {_SAVED_MODEL_SIGNATURE_KEY: root.run})

# Run TRT conversion.
converter = self._CreateConverterV2(input_saved_model_dir)
converter.convert()

# Verify the converted GraphDef and ConcreteFunction.
self._CheckTrtOps(converter._converted_func)  # pylint: disable=protected-access

trt_engine_name = self._GetUniqueTRTEngineOp(
    converter._converted_graph_def).name

# Save the converted model without any TRT engine cache.
output_saved_model_dir = self.mkdtemp()
converter.save(output_saved_model_dir)
unexpected_asset_file = \
        self._GetAssetFile(output_saved_model_dir, trt_engine_name)
self.assertFalse(os.path.exists(unexpected_asset_file))

# Run the converted function to populate the engine cache.
converter.build(input_fn=InputFunc)

# Save the converted model again with serialized engine cache.
output_saved_model_dir = self.mkdtemp()
converter.save(output_saved_model_dir)
expected_asset_file = \
        self._GetAssetFile(output_saved_model_dir, trt_engine_name)
self.assertTrue(os.path.exists(expected_asset_file))
self.assertTrue(os.path.getsize(expected_asset_file))

del converter
exit((output_saved_model_dir, expected_output))
