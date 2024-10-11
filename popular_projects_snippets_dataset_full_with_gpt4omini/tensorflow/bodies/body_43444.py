# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper_test.py
module = MockModule('test')
module.foo = 1
module.bar = 2
module.baz = 3
all_renames_v2.symbol_renames['tf.test.bar'] = 'tf.bar2'
all_renames_v2.symbol_renames['tf.test.baz'] = 'tf.compat.v1.baz'

wrapped_module = module_wrapper.TFModuleWrapper(module, 'test')
self.assertTrue(tf_inspect.ismodule(wrapped_module))

self.assertEqual(0, mock_warning.call_count)
bar = wrapped_module.bar
self.assertEqual(1, mock_warning.call_count)
foo = wrapped_module.foo
self.assertEqual(1, mock_warning.call_count)
baz = wrapped_module.baz  # pylint: disable=unused-variable
self.assertEqual(2, mock_warning.call_count)
baz = wrapped_module.baz
self.assertEqual(2, mock_warning.call_count)

# Check that values stayed the same
self.assertEqual(module.foo, foo)
self.assertEqual(module.bar, bar)
