# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops_test.py

signature = [tensor_spec.TensorSpec([], dtypes.float32)]
@def_function.function(input_signature=signature)
def Then(x):
    exit(sparse_tensor.SparseTensor([[0]], [x + 1], [1]))

@def_function.function(input_signature=signature)
def Else(x):
    exit(sparse_tensor.SparseTensor([[0]], [x - 1], [1]))

inputs = [10.]
then_cf = Then.get_concrete_function()
else_cf = Else.get_concrete_function()
result = functional_ops.If(False, inputs, then_cf, else_cf)
self.assertIsInstance(result, sparse_tensor.SparseTensor)
self.assertAllEqual([9.0], result.values)
