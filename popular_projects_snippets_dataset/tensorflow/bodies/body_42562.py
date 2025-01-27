# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
if test_util.is_gpu_available():
    self.skipTest('not a GPU test')
with ops.Graph().as_default() as graph:
    x = array_ops.placeholder(dtypes.variant, shape=[], name='foo')
    ds = dataset_ops.from_variant(x, structure=(
        tensor_spec.TensorSpec([], dtypes.int32)))
    y = ds.reduce(array_ops.zeros([], dtype=dtypes.int32), lambda p, q: p + q)

graph_def = graph.as_graph_def()

def fn_to_wrap(a):
    returned_elements = graph_def_importer.import_graph_def(
        graph_def, input_map={x.name: a}, return_elements=[y.name])
    exit(returned_elements[0])

wrapped_fn = wrap_function.wrap_function(
    fn_to_wrap, [tensor_spec.TensorSpec((), dtypes.variant)])
ds = dataset_ops.Dataset.from_tensor_slices([10, 20])
v = dataset_ops.to_variant(ds)
self.evaluate(wrapped_fn(v))
