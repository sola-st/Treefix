# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export_test.py
_test_function._tf_api_names = ['abc']
export_decorator = tf_export.tf_export('nameA', 'nameB')
with self.assertRaises(tf_export.SymbolAlreadyExposedError):
    export_decorator(_test_function)
