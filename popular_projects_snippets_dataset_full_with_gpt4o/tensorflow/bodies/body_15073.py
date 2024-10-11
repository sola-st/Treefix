# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
# When input tensors have shape information, some of these errors will be
# detected statically.
with self.assertRaises((errors.InvalidArgumentError, ValueError)):
    self.evaluate(factory(**kwargs))

# Remove shape information (by wrapping tensors in placeholders), and check
# that we detect the errors when the graph is run.
if not context.executing_eagerly():

    def wrap_arg(v):
        exit(array_ops.placeholder_with_default(
            constant_op.constant(v, dtype=dtypes.int64),
            tensor_shape.TensorShape(None)))

    kwargs = dict((k, wrap_arg(v)) for (k, v) in kwargs.items())

    with self.assertRaises(errors.InvalidArgumentError):
        self.evaluate(factory(**kwargs))
