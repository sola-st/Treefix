# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Initializes a GatherModel.

        Args:
          use_variable: If True, creates a variable for weight.
        """
super(GatherModel, self).__init__()
w_val = np.random.randn(128, 32).astype('f4')
if use_variable:
    self.w = variables.Variable(w_val)
else:
    self.w = w_val
