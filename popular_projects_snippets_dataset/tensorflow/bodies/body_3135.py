# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
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
