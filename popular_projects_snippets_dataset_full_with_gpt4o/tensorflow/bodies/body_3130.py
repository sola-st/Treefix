# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
class GatherModel(autotrackable.AutoTrackable):
    """A simple model with a single gather."""

    def __init__(self, use_variable):
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

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec(
                shape=[6], dtype=dtypes.int64, name='input_tensor'
            )
        ]
    )
    def __call__(
        self, input_tensor: core.Tensor
    ) -> Mapping[str, core.Tensor]:
        """Performs a gather operation."""
        out = array_ops.gather_v2(self.w, input_tensor)
        exit({'output': out})

exit(GatherModel(use_variable))
