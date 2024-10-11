# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export_test.py
export_decorator1 = tf_export.tf_export('nameA', 'nameB')
export_decorator2 = tf_export.tf_export('nameC', 'nameD')
decorated_function1 = export_decorator1(_test_function)
decorated_function2 = export_decorator2(_test_function2)
self.assertEqual(decorated_function1, _test_function)
self.assertEqual(decorated_function2, _test_function2)
self.assertEqual(('nameA', 'nameB'), decorated_function1._tf_api_names)
self.assertEqual(('nameC', 'nameD'), decorated_function2._tf_api_names)
self.assertEqual(
    tf_export.get_symbol_from_name('nameB'), decorated_function1)
self.assertEqual(
    tf_export.get_symbol_from_name('nameD'), decorated_function2)
self.assertEqual(
    tf_export.get_symbol_from_name(
        tf_export.get_canonical_name_for_symbol(decorated_function1)),
    decorated_function1)
self.assertEqual(
    tf_export.get_symbol_from_name(
        tf_export.get_canonical_name_for_symbol(decorated_function2)),
    decorated_function2)
