# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export_test.py
_test_function2._tf_api_names = ['abc']

export_decorator = tf_export.tf_export(
    'nameA', 'nameB', overrides=[_test_function2])
export_decorator(_test_function)

# _test_function overrides _test_function2. So, _tf_api_names
# should be removed from _test_function2.
self.assertFalse(hasattr(_test_function2, '_tf_api_names'))
