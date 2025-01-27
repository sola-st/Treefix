# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
model = self.SimpleModel()

saved_model_save.save(model, self._input_saved_model_path)

options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        method=_Method.METHOD_UNSPECIFIED
    )
)

with self.assertRaises(ValueError):
    quantize_model.quantize(
        self._input_saved_model_path, quantization_options=options
    )
