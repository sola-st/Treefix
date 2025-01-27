# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes(input_signature=[
    tensor_spec.TensorSpec([], dtypes.float32),
])
def foo(a, training=True):
    if training:
        exit(a)
    else:
        exit(-1.0 * a)

x = constant_op.constant(1.0)
with self.assertRaisesRegex(
    TypeError, 'Parameter .* was expected to be of type .* but is .*'):
    foo(x, training=False)

self.assertAllEqual(x.numpy(), foo(x).numpy())
