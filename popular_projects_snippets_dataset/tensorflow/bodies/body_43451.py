# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper_test.py
self.assertFalse(module_wrapper.TFModuleWrapper.compat_v1_usage_recorded)
apis = {'cosh': ('', 'cmd')}

mock_tf = MockModule('tensorflow')
mock_tf_wrapped = module_wrapper.TFModuleWrapper(
    mock_tf, 'test', public_apis=apis)
mock_tf_wrapped.cosh  # pylint: disable=pointless-statement
self.assertFalse(module_wrapper.TFModuleWrapper.compat_v1_usage_recorded)

mock_tf_v1 = MockModule('tensorflow.compat.v1')
mock_tf_v1_wrapped = module_wrapper.TFModuleWrapper(
    mock_tf_v1, 'test', public_apis=apis)
self.assertFalse(module_wrapper.TFModuleWrapper.compat_v1_usage_recorded)
mock_tf_v1_wrapped.cosh  # pylint: disable=pointless-statement
self.assertTrue(module_wrapper.TFModuleWrapper.compat_v1_usage_recorded)

# 'Reset' the status before testing against 'tensorflow.compat.v2.compat.v1'
module_wrapper.TFModuleWrapper.compat_v1_usage_recorded = False
mock_tf_v2_v1 = mock_tf_v1 = MockModule('tensorflow.compat.v2.compat.v1')
mock_tf_v2_v1_wrapped = module_wrapper.TFModuleWrapper(
    mock_tf_v2_v1, 'test', public_apis=apis)
self.assertFalse(module_wrapper.TFModuleWrapper.compat_v1_usage_recorded)
mock_tf_v2_v1_wrapped.cosh  # pylint: disable=pointless-statement
self.assertTrue(module_wrapper.TFModuleWrapper.compat_v1_usage_recorded)
