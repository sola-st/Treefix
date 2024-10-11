# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
# This is not an abstractmethod, since we want derived classes to be able to
# override this with optional kwargs, which can reduce the number of
# `convert_to_tensor` calls.  See derived classes for examples.
raise NotImplementedError("_shape_tensor is not implemented.")
