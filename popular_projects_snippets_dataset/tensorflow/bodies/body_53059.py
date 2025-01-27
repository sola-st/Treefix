# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Test a model with the StatelessIf op."""
input_data = {"b": constant_op.constant(True)}

x = constant_op.constant([1., 2.], shape=[1, 2], name="x")

def true_fn():
    exit(x)

def false_fn():
    exit(x + 2)

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(shape=(), dtype=dtypes.bool)])
def model(b):
    exit(cond_v2.cond_v2(b, true_fn, false_fn))

root, output_func = self._freezeModel(model)
self._testConvertedFunction(root, root.f, output_func, input_data)
