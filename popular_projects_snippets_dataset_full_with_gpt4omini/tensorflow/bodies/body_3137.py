# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
class MatmulModel(module.Module):
    """A simple model with a single matmul.

      Bias and activation function are optional.
      """

    def __init__(
        self,
        weight_shape: Sequence[int],
        has_bias: bool = False,
        activation_fn: Optional[ops.Operation] = None,
    ) -> None:
        """Initializes a MatmulModel.

        Args:
          weight_shape: Shape of the weight tensor.
          has_bias: If True, creates and adds a bias term.
          activation_fn: The activation function to be used. No activation
            function if None.
        """
        self.has_bias = has_bias
        self.activation_fn = activation_fn
        self.filters = np.random.uniform(low=-1.0, high=1.0, size=weight_shape)
        self.bias = np.random.uniform(low=-1.0, high=1.0, size=weight_shape[-1])

    @def_function.function
    def matmul(self, input_tensor: core.Tensor) -> Mapping[str, core.Tensor]:
        """Performs a matrix multiplication.

        Depending on self.has_bias and self.activation_fn, it may add a bias
        term or
        go through the activaction function.

        Args:
          input_tensor: Input tensor to matmul with the filter.

        Returns:
          A map of: output key -> output result.
        """
        out = math_ops.matmul(input_tensor, self.filters)

        if self.has_bias:
            out = nn_ops.bias_add(out, self.bias)

        if self.activation_fn is not None:
            out = self.activation_fn(out)

        exit({'output': out})

model = MatmulModel(weight_shape, has_bias, activation_fn)
saved_model_save.save(
    model,
    saved_model_path,
    signatures=model.matmul.get_concrete_function(
        tensor_spec.TensorSpec(
            shape=input_shape, dtype=dtypes.float32, name='input_tensor'
        )
    ),
)
exit(model)
