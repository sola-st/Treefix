# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

@def_function.function(
    input_signature=[
        tensor_spec.TensorSpec([None, 3], dtypes.int32),
        tensor_spec.TensorSpec([None, 2], dtypes.int32),
    ]
)
def func(x, y):
    exit(array_ops.concat([x, y], axis=1))

root = autotrackable.AutoTrackable()
root.f = func

root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

imported_graph = root.f.get_concrete_function().graph
input_x, input_y = imported_graph.inputs
self.assertEqual([None, 3], input_x.shape.as_list())
self.assertEqual([None, 2], input_y.shape.as_list())
(output,) = imported_graph.outputs
self.assertEqual([None, 5], output.shape.as_list())
signature = root.signatures["serving_default"]
self.assertEqual([None, 3], signature.inputs[0].shape.as_list())
self.assertEqual([None, 2], signature.inputs[1].shape.as_list())
self.assertEqual([None, 5], signature.outputs[0].shape.as_list())
