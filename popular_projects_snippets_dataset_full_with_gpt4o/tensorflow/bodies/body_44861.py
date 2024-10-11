# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/function_wrappers_test.py
if context.executing_eagerly():
    self.skipTest('Tensor names are disabled in eager')

with function_wrappers.FunctionScope(
    'test_name', None,
    converter.ConversionOptions(
        optional_features=converter.Feature.NAME_SCOPES)):
    t = constant_op.constant(1)
self.assertIn('test_name', t.name)
