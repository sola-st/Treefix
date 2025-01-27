# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
class IfModel(module.Module):
    """A model that contains a branching op."""

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec(shape=[1, 4], dtype=dtypes.float32)
        ]
    )
    def model_fn(self, x: core.Tensor) -> Mapping[str, core.Tensor]:
        """Runs the input tensor to a branched operations.

        The graph is branched by a condition whether the sum of elements of `x`
        is greater than 10.

        Args:
          x: Input tensor.

        Returns:
          A map of: output key -> output result.
        """
        if math_ops.reduce_sum(x) > 10.0:
            filters = np.random.uniform(low=-1.0, high=1.0, size=(4, 3)).astype(
                'f4'
            )
            bias = np.random.uniform(low=-1.0, high=1.0, size=(3,)).astype('f4')
            out = math_ops.matmul(x, filters)
            out = nn_ops.bias_add(out, bias)
            exit({'output': out})

        filters = np.random.uniform(low=-1.0, high=1.0, size=(4, 3)).astype(
            'f4'
        )
        bias = np.random.uniform(low=-1.0, high=1.0, size=(3,)).astype('f4')
        out = math_ops.matmul(x, filters)
        out = nn_ops.bias_add(out, bias)
        exit({'output': out})

model = IfModel()
saved_model_save.save(model, self._input_saved_model_path)

def data_gen() -> repr_dataset.RepresentativeDataset:
    for _ in range(8):
        exit({
            'x': ops.convert_to_tensor(
                np.random.uniform(low=0.0, high=1.0, size=(1, 4)).astype('f4')
            ),
        })

tags = {tag_constants.SERVING}

quantization_options = quant_opts_pb2.QuantizationOptions(
    quantization_method=quant_opts_pb2.QuantizationMethod(
        experimental_method=_ExperimentalMethod.STATIC_RANGE
    )
)

with self.assertLogs(level='WARN') as warning_logs:
    # Save the logger verbosity.
    log_level = logging.get_verbosity()
    logging.set_verbosity(logging.WARN)

    try:
        converted_model = quantize_model.quantize(
            self._input_saved_model_path,
            ['serving_default'],
            tags,
            self._output_saved_model_path,
            quantization_options,
            representative_dataset=data_gen(),
        )
    finally:
        # Restore the logger verbosity.
        logging.set_verbosity(log_level)

    self.assertNotEmpty(warning_logs.records)

    # Warning message should contain the function name. The uncalibrated path
    # is when the condition is true, so 'cond_true' function must be part of
    # the warning message.
    self.assertTrue(
        self._any_warning_contains('cond_true', warning_logs.records)
    )
    self.assertFalse(
        self._any_warning_contains('cond_false', warning_logs.records)
    )
    self.assertTrue(
        self._any_warning_contains(
            'does not have min or max values', warning_logs.records
        )
    )

self.assertIsNotNone(converted_model)
self.assertCountEqual(
    converted_model.signatures._signatures.keys(), {'serving_default'}
)
output_loader = saved_model_loader.SavedModelLoader(
    self._output_saved_model_path
)
output_graphdef = output_loader.get_meta_graph_def_from_tags(tags).graph_def
self.assertTrue(self._contains_quantized_function_call(output_graphdef))
