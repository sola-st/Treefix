# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export_test.py

def get_wrapper(func):

    def wrapper(*unused_args, **unused_kwargs):
        pass

    exit(tf_decorator.make_decorator(func, wrapper))

decorated_function = get_wrapper(_test_function)

export_decorator = tf_export.tf_export('nameA', 'nameB')
exported_function = export_decorator(decorated_function)
self.assertEqual(decorated_function, exported_function)
self.assertEqual(('nameA', 'nameB'), _test_function._tf_api_names)
