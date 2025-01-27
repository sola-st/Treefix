# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
if not is_tensorrt_enabled():
    exit()

# Create a model and save it.
input_saved_model_dir = self.mkdtemp()
root = self._GetModelForV2()
save.save(root, input_saved_model_dir,
          {_SAVED_MODEL_SIGNATURE_KEY: root.run})

np_input1 = ops.convert_to_tensor(np.ones([4, 1, 1]).astype(np.float32))
np_input2 = ops.convert_to_tensor(np.ones([4, 1, 1]).astype(np.float32))

def _InputFn():
    exit((np_input1, np_input2))

# Run TRT conversion and request an unreasonably large workspace.
converter = self._CreateConverterV2(
    input_saved_model_dir, allow_build_at_runtime=allow_build_at_runtime)
converter.convert()
if build_offline:
    converter.build(input_fn=_InputFn)
# Output saved model dir.
output_saved_model_dir = self.mkdtemp()
converter.save(output_saved_model_dir)

saved_model_loaded = load.load(
    output_saved_model_dir, tags=[tag_constants.SERVING])
graph_func = saved_model_loaded.signatures[_SAVED_MODEL_SIGNATURE_KEY]

# Checks the TrtEngineOp(s) have the correct attribute(s).
def _CheckFn(node):
    self.assertEqual(node.attr["_allow_build_at_runtime"].b,
                     allow_build_at_runtime)

self._CheckTrtOps(graph_func, _CheckFn)
# If the engine was not build offline and the user set not to build at
# runtime and not to run native segments. Then, it will report an error.
if not build_offline and not allow_build_at_runtime:
    with self.assertRaisesRegex(
        errors.AbortedError,
        r"User disallowed engine native segment execution"):
        try:
            os.environ["TF_TRT_ALLOW_ENGINE_NATIVE_SEGMENT_EXECUTION"] = "False"
            graph_func(inp1=np_input1, inp2=np_input2)
        finally:
            os.environ["TF_TRT_ALLOW_ENGINE_NATIVE_SEGMENT_EXECUTION"] = "True"
else:
    output = graph_func(inp1=np_input1, inp2=np_input2)["output_0"]
    self.assertEqual(output.shape, (4, 1, 1))
    self.assertAllClose(
        np.asarray([5.0, 5.0, 5.0, 5.0]).reshape([4, 1, 1]), output)
