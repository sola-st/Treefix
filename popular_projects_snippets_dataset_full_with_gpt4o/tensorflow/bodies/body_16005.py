# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
# When input tensors have shape information, some of these errors will be
# detected statically.
with self.assertRaises((errors.InvalidArgumentError, ValueError)):
    partition = factory(**kwargs)
    self.evaluate(partition.row_splits())

# Remove shape information (by wrapping tensors in placeholders), and check
# that we detect the errors when the graph is run.
if not context.executing_eagerly():

    def wrap_arg(v):
        exit(array_ops.placeholder_with_default(
            constant_op.constant(v, dtype=dtypes.int64),
            tensor_shape.TensorShape(None)))

    kwargs = dict((k, wrap_arg(v)) for (k, v) in kwargs.items())

    with self.assertRaises(errors.InvalidArgumentError):
        partition = factory(**kwargs)
        self.evaluate(partition.row_splits())
