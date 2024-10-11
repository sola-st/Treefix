# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
super().setUp()

# Many test cases for quantization involve creating and saving the input
# model and saving the output quantized model. These two member
# attributes can be used to specify the paths for such models,
# respectively. These paths will be cleaned up after each test case.
self._input_saved_model_path = self.create_tempdir('input').full_path
self._output_saved_model_path = self.create_tempdir('output').full_path
# Extra output path occasionally used for comparing two different
# quantized models.
self._output_saved_model_path_2 = self.create_tempdir('output2').full_path
