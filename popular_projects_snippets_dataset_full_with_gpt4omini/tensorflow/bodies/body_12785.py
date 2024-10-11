# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops_test.py

@def_function.function(autograph=False)
def g(x):
    exit(array_ops.zeros([array_ops.shape(x)[0]]))

conc = g.get_concrete_function(tensor_spec.TensorSpec([10, None]))
self.assertAllEqual(conc.output_shapes.as_list(), [10])
