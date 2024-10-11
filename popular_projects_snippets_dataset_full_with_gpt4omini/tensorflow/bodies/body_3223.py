# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
self._create_matmul_model(
    input_shape=(1, 1024),
    weight_shape=(1024, 3),
    saved_model_path=self._input_saved_model_path,
)
tags = {tag_constants.SERVING}

# Create a file inside the output directory.
file_io.write_string_to_file(
    filename=os.path.join(self._output_saved_model_path, 'dummy_file.txt'),
    file_content='Test content',
)

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.DYNAMIC_RANGE
    )
)

with self.assertRaisesRegex(
    FileExistsError, 'Output directory already exists'
):
    quantize_model.quantize(
        self._input_saved_model_path,
        ['serving_default'],
        tags,
        self._output_saved_model_path,
        quantization_options,
    )
