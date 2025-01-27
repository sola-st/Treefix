# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Testing ShapeOp and int32 values as engine input and output."""
np_input = np.random.random_sample([5, 3]).astype(np.float32)

def _InputFunc():
    # Passing single input parameter as a tuple with one element
    exit((np_input,))

output_saved_model_dir, expected_output = \
        self._BuildGraphWithInputGenerator(_InputFunc, np_input)

root_with_trt = load.load(output_saved_model_dir)
converted_signature = root_with_trt.signatures["serving_default"]
# Check that the graph is converted to two TRTEngineOps.
self._CheckTrtOps(converted_signature, num_engines=2)
# Run the graph.
output_with_trt = converted_signature(x=ops.convert_to_tensor(np_input))
# Check the result of the run.
self.assertAllClose(expected_output, list(output_with_trt.values())[0])
