# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
"""Checks that Variables in `obj` have equivalent Tensors in `tensor_obj."""
if isinstance(obj, variables.Variable):
    self.assertAllClose(ops.convert_to_tensor(obj),
                        ops.convert_to_tensor(tensor_obj))
elif isinstance(obj, composite_tensor.CompositeTensor):
    params = getattr(obj, "parameters", {})
    tensor_params = getattr(tensor_obj, "parameters", {})
    self.assertAllEqual(params.keys(), tensor_params.keys())
    self._check_tensors_equal_variables(params, tensor_params)
elif nest.is_mapping(obj):
    for k, v in obj.items():
        self._check_tensors_equal_variables(v, tensor_obj[k])
elif nest.is_nested(obj):
    for x, y in zip(obj, tensor_obj):
        self._check_tensors_equal_variables(x, y)
else:
    # We only check Tensor, CompositeTensor, and nested structure parameters.
    pass
