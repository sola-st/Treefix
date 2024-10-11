# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
if callable(fields):
    fields = fields()  # deferred construction: fields may include tensors.
if callable(nrows):
    nrows = nrows()  # deferred construction.
if callable(row_partitions):
    row_partitions = row_partitions()  # deferred construction.
for validate in (True, False):
    struct = StructuredTensor.from_fields(
        fields,
        shape,
        nrows=nrows,
        row_partitions=row_partitions,
        validate=validate)
    if expected_shape is None:
        expected_shape = shape
    self.assertEqual(struct.shape.as_list(), expected_shape)
    self.assertLen(expected_shape, struct.rank)
    self.assertCountEqual(struct.field_names(), tuple(fields.keys()))
    for field, value in fields.items():
        self.assertIsInstance(
            struct.field_value(field),
            (ops.Tensor, structured_tensor.StructuredTensor,
             ragged_tensor.RaggedTensor))
        self.assertAllEqual(struct.field_value(field), value)
