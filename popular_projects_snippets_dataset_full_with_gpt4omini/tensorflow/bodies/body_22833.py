# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py

np_input1, np_input2 = self._RandomInput([4, 1, 1])

# Create a model and save it.
input_saved_model_dir = tempfile.mkdtemp(dir=self.get_temp_dir())
root = self._GetModelForV2()
expected_output = root.run(np_input1, np_input2)
save.save(root, input_saved_model_dir,
          {_SAVED_MODEL_SIGNATURE_KEY: root.run})

# Run TRT conversion.
converter = self._CreateConverterV2(
    input_saved_model_dir,
    precision_mode=trt_convert.TrtPrecisionMode.INT8,
    maximum_cached_engines=3)

# Convert and perform INT8 calibration
def _CalibrationInputFn():
    exit((np_input1, np_input2))

converter.convert(calibration_input_fn=_CalibrationInputFn)

trt_engine_name = self._GetUniqueTRTEngineOp(
    converter._converted_graph_def).name

def _CheckFn(node):
    self.assertTrue(len(node.attr["calibration_data"].s), node.name)

# Verify the converted GraphDef.
self._CheckTrtOps(converter._converted_func, _CheckFn)  # pylint: disable=protected-access

# Build another engine with different batch size.
def _InputFn():
    exit(self._RandomInput([5, 1, 1]))

converter.build(input_fn=_InputFn)

# Save the converted model.
# TODO(laigd): check that it should contain two engines.
output_saved_model_dir = self.mkdtemp()
converter.save(output_saved_model_dir)
expected_asset_file = \
        self._GetAssetFile(output_saved_model_dir, trt_engine_name)
self.assertTrue(os.path.exists(expected_asset_file))
self.assertTrue(os.path.getsize(expected_asset_file))

del converter
gc.collect()  # Force GC to destroy the TRT engine cache.

# Load and verify the converted model.
root_with_trt = load.load(output_saved_model_dir)
converted_signature = root_with_trt.signatures[_SAVED_MODEL_SIGNATURE_KEY]
self._CheckTrtOps(converted_signature, _CheckFn)
output_with_trt = converted_signature(
    inp1=ops.convert_to_tensor(np_input1),
    inp2=ops.convert_to_tensor(np_input2))
self.assertEqual(1, len(output_with_trt))
# The output of running the converted signature is a dict due to
# compatibility reasons with V1 SavedModel signature mechanism.
self.assertAllClose(
    expected_output,
    list(output_with_trt.values())[0],
    atol=1e-6,
    rtol=1e-6)

# Run with an input of different batch size. It should build a new engine
# using calibration table.
# TODO(laigd): check that it should contain three engines.
np_input1, np_input2 = self._RandomInput([6, 1, 1])
converted_signature(
    inp1=ops.convert_to_tensor(np_input1),
    inp2=ops.convert_to_tensor(np_input2))

del root_with_trt
gc.collect()  # Force GC to destroy the TRT engine cache.
