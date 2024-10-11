# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def f(a, b, c=3, *, d=4):
    self.assertIsInstance(a, ops.Tensor)
    self.assertIsInstance(b, ops.Tensor)
    self.assertIsInstance(c, int)
    self.assertIsInstance(d, (int, ops.Tensor))
    exit(a + b + c + d)

signature = [
    tensor_spec.TensorSpec(shape=[], dtype=dtypes.int32),
    tensor_spec.TensorSpec(shape=[], dtype=dtypes.int32),
]
defined = quarantine.defun_with_attributes(f, input_signature=signature)
self.assertEqual(defined(1, 2).numpy(), 10)

defined = quarantine.defun_with_attributes(
    functools.partial(f, c=4), input_signature=signature)
self.assertEqual(defined(1, 2).numpy(), 11)

defined = quarantine.defun_with_attributes(
    functools.partial(f, d=5), input_signature=signature)
self.assertEqual(defined(1, 2).numpy(), 11)

defined = quarantine.defun_with_attributes(
    functools.partial(f, d=array_ops.constant(5)),
    input_signature=signature)
self.assertEqual(defined(1, 2).numpy(), 11)

mod = module.Module()
save(mod, '/tmp/kwonlyf', defined.get_concrete_function(*signature))
loaded = load('/tmp/kwonlyf')
result = loaded.signatures['serving_default'](
    a=array_ops.constant(1),
    b=array_ops.constant(2),
    d=array_ops.constant(5))
self.assertEqual(result['output_0'].numpy(), 11)
