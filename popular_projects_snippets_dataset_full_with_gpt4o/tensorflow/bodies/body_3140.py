# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
class EinsumModel(module.Module):
    """A simple model with a single einsum.

      Bias and activation function are optional.
      """

    def __init__(
        self,
        equation: str,
        weight_shape: Sequence[int],
        bias_shape: Optional[Sequence[int]] = None,
        activation_fn: Optional[ops.Operation] = None,
    ) -> None:
        """Initializes a EinsumModel.

        Args:
          equation: a string describing the contraction.
          weight_shape: Shape of the weight tensor.
          bias_shape: Shape of the bias. This is not always 1D so Einsum ops
            usually use Add op instead of BiasAdd.
          activation_fn: The activation function to be used. No activation
            function if None.
        """
        self.equation = equation
        self.activation_fn = activation_fn
        self.weight = np.random.uniform(low=-1.0, high=1.0, size=weight_shape)
        self.bias = (
            np.random.uniform(low=-1.0, high=1.0, size=bias_shape)
            if bias_shape is not None
            else None
        )

    @def_function.function
    def einsum(self, input_tensor: core.Tensor) -> Mapping[str, core.Tensor]:
        """Evaluates the Einstein summation convention.

        Depending on self.has_bias and self.activation_fn, it may add a bias
        term or go through the activaction function.

        Args:
          input_tensor: Input tensor to einsum with the weight.

        Returns:
          A map of: output key -> output result.
        """
        out = tensorflow.einsum(self.equation, input_tensor, self.weight)

        if self.bias is not None:
            out = out + self.bias

        if self.activation_fn is not None:
            out = self.activation_fn(out)

        exit({'output': out})

model = EinsumModel(equation, weight_shape, bias_shape, activation_fn)
saved_model_save.save(
    model,
    saved_model_path,
    signatures=model.einsum.get_concrete_function(
        tensor_spec.TensorSpec(
            shape=input_shape, dtype=dtypes.float32, name='input_tensor'
        )
    ),
)
exit(model)
