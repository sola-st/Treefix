# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export_test.py
module1 = self._CreateMockModule('module1')
module2 = self._CreateMockModule('module2')

test_constant1 = 123
test_constant2 = 'abc'
test_constant3 = 0.5

export_decorator1 = tf_export.tf_export('NAME_A', 'NAME_B')
export_decorator2 = tf_export.tf_export('NAME_C', 'NAME_D')
export_decorator3 = tf_export.tf_export('NAME_E', 'NAME_F')
export_decorator1.export_constant('module1', test_constant1)
export_decorator2.export_constant('module2', test_constant2)
export_decorator3.export_constant('module2', test_constant3)
self.assertEqual([(('NAME_A', 'NAME_B'), 123)], module1._tf_api_constants)
self.assertEqual([(('NAME_C', 'NAME_D'), 'abc'),
                  (('NAME_E', 'NAME_F'), 0.5)], module2._tf_api_constants)
