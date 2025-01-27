# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
# First lets assert the structure is the same.
self.assertTrue(
    structure.are_compatible(ds1.element_spec, ds2.element_spec))

# Now create iterators on both and assert they produce the same values.
it1 = dataset_ops.make_initializable_iterator(ds1)
it2 = dataset_ops.make_initializable_iterator(ds2)

get_next1 = it1.get_next()
get_next2 = it2.get_next()

with self.cached_session():
    self.evaluate([it1.initializer, it2.initializer])
    val1, val2 = self.evaluate([get_next1, get_next2])
    self.assertEqual(val1, val2)
