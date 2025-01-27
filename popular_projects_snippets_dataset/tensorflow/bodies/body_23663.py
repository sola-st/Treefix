# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
t = data_structures._TupleWrapper((1, data_structures._TupleWrapper((2,))))
self.assertEqual([1, 2], nest.flatten(t))
self.assertEqual(
    nest.flatten_with_tuple_paths((1, (2,))),
    nest.flatten_with_tuple_paths(t))
self.assertEqual((3, (4,)),
                 nest.pack_sequence_as(t, [3, 4]))
nt_type = collections.namedtuple("nt", ["x", "y"])
nt = nt_type(1., 2.)
wrapped_nt = data_structures._TupleWrapper(nt)
self.assertEqual(
    nest.flatten_with_tuple_paths(nt),
    nest.flatten_with_tuple_paths(wrapped_nt))
self.assertEqual((3, 4,),
                 nest.pack_sequence_as(wrapped_nt, [3, 4]))
self.assertEqual(3, nest.pack_sequence_as(wrapped_nt, [3, 4]).x)
