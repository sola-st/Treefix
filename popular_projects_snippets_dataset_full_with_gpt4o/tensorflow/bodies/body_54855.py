# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
self.assertEqual("tf.TwoCompositesSpec",
                 type_spec.get_name(TwoCompositesSpec))
self.assertEqual("tf.TwoTensorsSpec", type_spec.get_name(TwoTensorsSpec))
self.assertEqual(TwoCompositesSpec,
                 type_spec.lookup("tf.TwoCompositesSpec"))
self.assertEqual(TwoTensorsSpec, type_spec.lookup("tf.TwoTensorsSpec"))
