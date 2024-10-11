# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def func(x, kangaroo=None, octopus=7):
    del octopus, kangaroo
    exit(x)

scalar = constant_op.constant(5)
vector = constant_op.constant([10, 10, 20])
ragged = ragged_factory_ops.constant([[10, 20], [40]])

c1 = func.get_concrete_function(scalar, vector)
c1_summary = r'func\(x, kangaroo, octopus=7\)'
c1_details = (r'  Args:\n'
              r'    x: int32 Tensor, shape=\(\)\n'
              r'    kangaroo: int32 Tensor, shape=\(3,\)\n'
              r'  Returns:\n'
              r'    int32 Tensor, shape=\(\)')
self.assertRegex(c1.pretty_printed_signature(verbose=False), c1_summary)
self.assertRegex(
    c1.pretty_printed_signature(verbose=True),
    c1_summary + '\n' + c1_details)
self.assertRegex(
    repr(c1), r'<ConcreteFunction func\(x, kangaroo, octopus=7\) at .*>')
self.assertRegex(
    str(c1), 'ConcreteFunction {}\n{}'.format(c1_summary, c1_details))

c2 = func.get_concrete_function(scalar, ragged, 3)
c2_summary = r'func\(x, kangaroo, octopus=3\)'
c2_details = (r'  Args:\n'
              r'    x: int32 Tensor, shape=\(\)\n'
              r'    kangaroo: RaggedTensorSpec\(.*\)\n'
              r'  Returns:\n'
              r'    int32 Tensor, shape=\(\)')
self.assertRegex(c2.pretty_printed_signature(),
                 c2_summary + '\n' + c2_details)

c3 = func.get_concrete_function({'a': scalar, 'b': [ragged, ragged]})
c3_summary = r'func\(x, kangaroo=None, octopus=7\)'
c3_details = (r'  Args:\n'
              r"    x: {'a': <1>, 'b': \[<2>, <3>\]}\n"
              r'      <1>: int32 Tensor, shape=\(\)\n'
              r'      <2>: RaggedTensorSpec\(.*\)\n'
              r'      <3>: RaggedTensorSpec\(.*\)\n'
              r'  Returns:\n'
              r"    {'a': <1>, 'b': \[<2>, <3>\]}\n"
              r'      <1>: int32 Tensor, shape=\(\)\n'
              r'      <2>: RaggedTensorSpec\(.*\)\n'
              r'      <3>: RaggedTensorSpec\(.*\)')

# python 3.5 does not gurantee deterministic iteration of dict contents
# which can lead mismatch on pretty_printed_signature output for "Args"
if sys.version_info >= (3, 6):
    self.assertRegex(c3.pretty_printed_signature(),
                     c3_summary + '\n' + c3_details)

# pylint: disable=keyword-arg-before-vararg
@polymorphic_function.function
def func2(x, y=3, *args, **kwargs):
    exit((x, y, args, kwargs))

c4 = func2.get_concrete_function(scalar, 4, 5, a=scalar)
c4_summary = 'func2(x, y=4, arg3=5, *, a)'
self.assertEqual(c4.pretty_printed_signature(verbose=False), c4_summary)

c5 = func2.get_concrete_function(8, vector)
c5_summary = 'func2(x=8, y)'
self.assertEqual(c5.pretty_printed_signature(verbose=False), c5_summary)
