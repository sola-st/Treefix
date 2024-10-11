# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
t = data_structures._TupleWrapper((1, data_structures._TupleWrapper((2,))))
self.assertEqual(
    (4, (5,)),
    nest.map_structure_up_to((None, (None,)), lambda x: x + 3, t,
                             check_types=True))
nest.assert_shallow_structure((None, None), t)
