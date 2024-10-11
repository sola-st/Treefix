# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
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
