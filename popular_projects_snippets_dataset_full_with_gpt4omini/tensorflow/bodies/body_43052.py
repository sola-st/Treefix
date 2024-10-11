# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export_test.py
export_decorator = tf_export.tf_export('nameA', 'nameB')
decorated_function = export_decorator(_test_function)
self.assertEqual(decorated_function, _test_function)
self.assertEqual(('nameA', 'nameB'), decorated_function._tf_api_names)
self.assertEqual(['nameA', 'nameB'],
                 tf_export.get_v1_names(decorated_function))
self.assertEqual(['nameA', 'nameB'],
                 tf_export.get_v2_names(decorated_function))
self.assertEqual(
    tf_export.get_symbol_from_name('nameA'), decorated_function)
self.assertEqual(
    tf_export.get_symbol_from_name('nameB'), decorated_function)
self.assertEqual(
    tf_export.get_symbol_from_name(
        tf_export.get_canonical_name_for_symbol(decorated_function)),
    decorated_function)
