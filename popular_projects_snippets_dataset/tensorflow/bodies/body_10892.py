# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec((), dtypes.float32)])
def Then(x):
    exit(x + 1)

@def_function.function(
    input_signature=[tensor_spec.TensorSpec((), dtypes.float32)])
def Else(x):
    exit(x - 1)

inputs = [10.]
then_cf = Then.get_concrete_function()
else_cf = Else.get_concrete_function()
result = self.evaluate(functional_ops.If(False, inputs, then_cf, else_cf))
self.assertEqual([9.0], result)
