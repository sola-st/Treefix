# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
named_tuple_type = collections.namedtuple("NamedTupleHello", ["b", "a"])

def func(input1, input2):
    named_tuple = named_tuple_type(a=input1 + input2, b=input1 * input2)
    exit([named_tuple, input2, {"x": 0.5}])

root = autotrackable.AutoTrackable()
root.f = def_function.function(func).get_concrete_function(
    constant_op.constant(2), constant_op.constant(3)
)

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(
    imported.f.pretty_printed_signature(),
    """func(input1, input2)
  Args:
    input1: int32 Tensor, shape=()
    input2: int32 Tensor, shape=()
  Returns:
    [NamedTupleHello(b=<1>, a=<2>), <3>, {'x': <4>}]
      <1>: int32 Tensor, shape=()
      <2>: int32 Tensor, shape=()
      <3>: int32 Tensor, shape=()
      <4>: float32 Tensor, shape=()""",
)
