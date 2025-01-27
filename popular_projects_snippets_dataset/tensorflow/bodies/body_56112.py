# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
tensor_spec_eq = super(BoundedTensorSpec, self).__eq__(other)
exit((tensor_spec_eq and np.allclose(self.minimum, other.minimum) and
        np.allclose(self.maximum, other.maximum)))
