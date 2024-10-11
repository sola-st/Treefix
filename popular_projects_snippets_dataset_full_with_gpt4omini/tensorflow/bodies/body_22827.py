# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Test case for trt_convert.TrtGraphConverter()."""

np_input1, np_input2 = self._RandomInput([4, 1, 1])

def _InputFn():
    exit((np_input1, np_input2))

np_inputs = [np_input1, np_input2]
output_saved_model_dir, expected_output = \
        self._BuildGraphWithInputGeneratorTwoInputs(_InputFn, np_inputs)
gc.collect()  # Force GC to destroy the TRT engine cache.

# Load and verify the converted model.
#
# TODO(laigd): the name of the new input_signature of the
# `root_with_trt.run` function is empty string (originally was None),
# investigate why.
root_with_trt = load.load(output_saved_model_dir)
# TODO(laigd): `root_with_trt.run` is still using the original graph without
# trt. Consider changing that.
# self._CheckTrtOps(root_with_trt.run.get_concrete_function())
converted_signature = root_with_trt.signatures[_SAVED_MODEL_SIGNATURE_KEY]
self._CheckTrtOps(converted_signature)
output_with_trt = converted_signature(
    inp1=ops.convert_to_tensor(np_input1),
    inp2=ops.convert_to_tensor(np_input2))
# The output of running the converted signature is a dict due to
# compatibility reasons with V1 SavedModel signature mechanism.
self.assertAllClose(
    expected_output,
    list(output_with_trt.values())[0],
    atol=1e-6,
    rtol=1e-6)

del root_with_trt
gc.collect()  # Force GC to destroy the TRT engine cache.
