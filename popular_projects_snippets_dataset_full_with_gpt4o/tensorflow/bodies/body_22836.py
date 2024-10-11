# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Test case for trt_convert.TrtGraphConverter()."""

np_input1, np_input2 = self._RandomInput([4, 1, 1])

# Create a model and save it.
input_saved_model_dir = self.mkdtemp()
root = self._GetModelForV2()
save.save(root, input_saved_model_dir,
          {_SAVED_MODEL_SIGNATURE_KEY: root.run})

# Run TRT conversion.
converter = self._CreateConverterV2(input_saved_model_dir)
converter.convert()

trt_engine_name = self._GetUniqueTRTEngineOp(
    converter._converted_graph_def).name

def _InputFn():
    exit((np_input1, np_input2))

converter.build(input_fn=_InputFn)  # Populate the TRT engine cache.
output_saved_model_dir = self.mkdtemp()
converter.save(output_saved_model_dir)

def _DestroyCache():
    with ops.device("GPU:0"):
        handle = gen_trt_ops.create_trt_resource_handle(
            resource_name=trt_engine_name)
        gen_resource_variable_ops.destroy_resource_op(
            handle, ignore_lookup_error=False)

with self.assertRaisesRegex(errors.NotFoundError,
                            r"Resource .* does not exist."):
    _DestroyCache()

# Load the converted model and make sure the engine cache is populated by
# default.
root = load.load(output_saved_model_dir)
_DestroyCache()
with self.assertRaisesRegex(errors.NotFoundError,
                            r"Resource .* does not exist."):
    _DestroyCache()

# Load the converted model again and make sure the engine cache is destroyed
# when the model goes out of scope.
root = load.load(output_saved_model_dir)
del root
gc.collect()  # Force GC to destroy the TRT engine cache.
with self.assertRaisesRegex(errors.NotFoundError,
                            r"Resource .* does not exist."):
    _DestroyCache()
