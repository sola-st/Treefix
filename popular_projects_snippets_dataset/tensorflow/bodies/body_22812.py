# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
# Create the SavedModel.
root = self._GetShapeOpModel()
expected_output = None if np_input is None else root.run(np_input)
input_saved_model_dir = self.mkdtemp()
save.save(root, input_saved_model_dir, signatures=root.run)

# Convert the graph to TF-TRT.
conv_params = trt_convert.TrtConversionParams(minimum_segment_size=2)
converter = trt_convert.TrtGraphConverterV2(
    input_saved_model_dir=input_saved_model_dir,
    use_dynamic_shape=True,
    **conv_params._asdict())
converter.convert()

# Build the graph with the input generator. This runs the TRTEngineOp native
# segment.
converter.build(InputFunc)
output_saved_model_dir = self.mkdtemp()
converter.save(output_saved_model_dir)
del converter
exit((output_saved_model_dir, expected_output))
