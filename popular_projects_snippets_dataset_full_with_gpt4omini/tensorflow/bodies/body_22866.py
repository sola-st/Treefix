# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Test case for trt_convert.TrtGraphConverter()."""

np_input1 = ops.convert_to_tensor(np.ones([4, 1, 1]).astype(np.float32))
np_input2 = ops.convert_to_tensor(np.ones([4, 1, 1]).astype(np.float32))

# Create a model and save it.
input_saved_model_dir = self.mkdtemp()
root = self._GetModelForV2()
save.save(root, input_saved_model_dir,
          {_SAVED_MODEL_SIGNATURE_KEY: root.run})

# Run TRT conversion.
converter = self._CreateConverterV2(
    input_saved_model_dir, precision_mode=trt_convert.TrtPrecisionMode.FP32)

converted_model = None
# Specify device on which converted model should be placed
with self.assertRaisesRegex(ValueError, r"Specified device is not a GPU"):
    with ops.device("CPU"):
        converted_model = converter.convert()

del converter
gc.collect()  # Force GC to destroy the TRT engine cache.
