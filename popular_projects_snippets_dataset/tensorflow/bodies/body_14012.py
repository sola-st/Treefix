# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
if callable(fields):
    fields = fields()  # deferred construction: fields may include tensors.

struct = StructuredTensor.from_fields_and_rank(fields, rank)
self.assertEqual(struct.shape.as_list(), expected_shape)
