# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
if callable(fields):
    fields = fields()  # deferred construction: fields may include tensors.
with self.assertRaisesRegex(ValueError, msg):
    StructuredTensor.from_fields_and_rank(fields, rank)
