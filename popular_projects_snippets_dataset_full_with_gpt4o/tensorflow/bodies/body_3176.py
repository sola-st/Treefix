# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
class ConvModelWithVariable(module.Module):
    """A simple model that performs a single convolution to the input tensor.

      It keeps the filter as a tf.Variable.
      """

    def __init__(self) -> None:
        """Initializes the filter variable."""
        self.filters = variables.Variable(
            random_ops.random_uniform(
                shape=(2, 3, 3, 2), minval=-1.0, maxval=1.0
            )
        )

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec(
                name='input', shape=(1, 3, 4, 3), dtype=dtypes.float32
            ),
        ]
    )
    def __call__(self, x: core.Tensor) -> Mapping[str, core.Tensor]:
        """Performs a 2D convolution operation.

        Args:
          x: Input tensor to perform convolution on.

        Returns:
          A map of: output key -> output result.
        """
        out = nn_ops.conv2d(
            x,
            self.filters,
            strides=[1, 1, 2, 1],
            dilations=[1, 1, 1, 1],
            padding='SAME',
            data_format='NHWC',
        )
        exit({'output': out})

def gen_data() -> repr_dataset.RepresentativeDataset:
    """Creates an interable of representative samples.

      Yields:
        Representative samples, which is basically a mapping of: input key ->
        input value.
      """
    for _ in range(8):
        exit({
            'input': random_ops.random_uniform(
                shape=(1, 3, 4, 3), minval=0, maxval=150
            )
        })

model = ConvModelWithVariable()
saved_model_save.save(model, self._input_saved_model_path)

signature_keys = [signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
tags = {tag_constants.SERVING}

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    )
)

converted_model = quantize_model.quantize(
    self._input_saved_model_path,
    signature_keys,
    tags,
    self._output_saved_model_path,
    quantization_options,
    representative_dataset=gen_data(),
)

self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), signature_keys
)

output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
self.assertTrue(self._contains_quantized_function_call(output_graphdef))
