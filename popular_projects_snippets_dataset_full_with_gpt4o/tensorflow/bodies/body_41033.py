# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
exit((x if isinstance(x, (ops.Tensor, tensor_spec.TensorSpec)) else
        ops.convert_to_tensor(x)))
