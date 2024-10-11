# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
np_input1, np_input2 = self._RandomInput([4, 1, 1])

# Create a model and save it.
input_saved_model_dir = self.mkdtemp()
root = self._GetModelForV2()
save.save(root, input_saved_model_dir,
          {_SAVED_MODEL_SIGNATURE_KEY: root.run})

def _InputFn():
    exit((np_input1, np_input2))

# Run TRT conversion
converter = self._CreateConverterV2(
    input_saved_model_dir, max_workspace_size_bytes=1 << 20)
converter.convert()

os.environ["TF_TRT_ALLOW_ENGINE_NATIVE_SEGMENT_EXECUTION"] = "False"
os.environ["TF_TRT_ABORT_CUDA_ENGINE_BUILD"] = "True"
with self.assertRaisesRegex(
    errors.AbortedError,
    r"User disallowed engine native segment execution"):
    try:
        converter.build(input_fn=_InputFn)
    finally:
        # Always reset the environment variable.
        os.environ["TF_TRT_ALLOW_ENGINE_NATIVE_SEGMENT_EXECUTION"] = "True"
        os.environ["TF_TRT_ABORT_CUDA_ENGINE_BUILD"] = "False"

converter.build(input_fn=_InputFn)
