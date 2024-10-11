# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export_test.py
export_decorator_a = tf_export.tf_export('TestClassA1')
export_decorator_a(TestClassA)
self.assertEqual(('TestClassA1',), TestClassA._tf_api_names)
self.assertTrue('_tf_api_names' not in TestClassB.__dict__)

export_decorator_b = tf_export.tf_export('TestClassB1')
export_decorator_b(TestClassB)
self.assertEqual(('TestClassA1',), TestClassA._tf_api_names)
self.assertEqual(('TestClassB1',), TestClassB._tf_api_names)
self.assertEqual(['TestClassA1'], tf_export.get_v1_names(TestClassA))
self.assertEqual(['TestClassB1'], tf_export.get_v1_names(TestClassB))
