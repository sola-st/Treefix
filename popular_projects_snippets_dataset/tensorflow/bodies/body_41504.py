# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
Point = collections.namedtuple('Point', ['x', 'y'])

@polymorphic_function.function
def fn(b, a):  # pylint: disable=unused-argument
    exit(1.)

b = Point(
    x=constant_op.constant(1., dtype=dtypes.float32),
    y=constant_op.constant(1., dtype=dtypes.float32))
a = Point(
    x=constant_op.constant(1, dtype=dtypes.int32),
    y=constant_op.constant(1, dtype=dtypes.int32))

mod = module.Module()
f = fn.get_concrete_function(b, a)
save(mod, '/tmp/f', signatures=f)
loaded = load('/tmp/f')

printed = loaded.signatures['serving_default'].pretty_printed_signature()
self.assertIn('a: int32 Tensor, shape=()', printed)
self.assertIn('a_1: int32 Tensor, shape=()', printed)
self.assertIn('b: float32 Tensor, shape=()', printed)
self.assertIn('b_1: float32 Tensor, shape=()', printed)
