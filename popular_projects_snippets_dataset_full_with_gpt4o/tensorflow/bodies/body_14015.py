# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
if not test_in_eager and context.executing_eagerly():
    exit()
if callable(fields):
    fields = fields()  # deferred construction.
if callable(nrows):
    nrows = nrows()  # deferred construction.
if callable(row_partitions):
    row_partitions = row_partitions()  # deferred construction.
with self.assertRaisesRegex(err, msg):
    struct = StructuredTensor.from_fields(
        fields=fields,
        shape=shape,
        nrows=nrows,
        row_partitions=row_partitions,
        validate=validate)
    for field_name in struct.field_names():
        self.evaluate(struct.field_value(field_name))
    self.evaluate(struct.nrows())
