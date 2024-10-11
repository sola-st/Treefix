# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
# ListWrapper, unlike List, compares like the built-in list type (since it
# is used to automatically replace lists).
a = autotrackable.AutoTrackable()
b = autotrackable.AutoTrackable()
self.assertEqual([a, a],
                 [a, a])
self.assertEqual(data_structures.ListWrapper([a, a]),
                 data_structures.ListWrapper([a, a]))
self.assertEqual([a, a],
                 data_structures.ListWrapper([a, a]))
self.assertEqual(data_structures.ListWrapper([a, a]),
                 [a, a])
self.assertNotEqual([a, a],
                    [b, a])
self.assertNotEqual(data_structures.ListWrapper([a, a]),
                    data_structures.ListWrapper([b, a]))
self.assertNotEqual([a, a],
                    data_structures.ListWrapper([b, a]))
self.assertLess([a], [a, b])
self.assertLess(data_structures.ListWrapper([a]),
                data_structures.ListWrapper([a, b]))
self.assertLessEqual([a], [a, b])
self.assertLessEqual(data_structures.ListWrapper([a]),
                     data_structures.ListWrapper([a, b]))
self.assertGreater([a, b], [a])
self.assertGreater(data_structures.ListWrapper([a, b]),
                   data_structures.ListWrapper([a]))
self.assertGreaterEqual([a, b], [a])
self.assertGreaterEqual(data_structures.ListWrapper([a, b]),
                        data_structures.ListWrapper([a]))
self.assertEqual([a], data_structures.ListWrapper([a]))
self.assertEqual([a], list(data_structures.List([a])))
self.assertEqual([a, a], data_structures.ListWrapper([a]) + [a])
self.assertEqual([a, a], [a] + data_structures.ListWrapper([a]))
self.assertIsInstance(data_structures.ListWrapper([a]), list)
self.assertEqual(
    tensor_shape.TensorShape([None, 2]).as_list(),
    (data_structures.ListWrapper([None])
     + tensor_shape.TensorShape([2])).as_list())
