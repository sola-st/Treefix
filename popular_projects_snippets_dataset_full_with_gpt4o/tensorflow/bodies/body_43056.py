# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export_test.py
module1 = self._CreateMockModule('module1')

export_decorator = tf_export.tf_export('NAME_A', 'NAME_B')
export_decorator.export_constant('module1', 'test_constant')
self.assertEqual([(('NAME_A', 'NAME_B'), 'test_constant')],
                 module1._tf_api_constants)
self.assertEqual([(('NAME_A', 'NAME_B'), 'test_constant')],
                 tf_export.get_v1_constants(module1))
self.assertEqual([(('NAME_A', 'NAME_B'), 'test_constant')],
                 tf_export.get_v2_constants(module1))
