# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
if callable(fields):
    fields = fields()
s = extension_type.AnonymousExtensionType(**fields)
for (name, value) in fields.items():
    actual = getattr(s, name)
    if isinstance(actual, (ops.Tensor, ragged_tensor.RaggedTensor)):
        self.assertAllEqual(actual, value)
    else:
        self.assertEqual(actual, value)
