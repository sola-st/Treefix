# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest_test.py
st = sparse_tensor.SparseTensorValue([[0]], [0], [1])
single_value = st
list_of_values = [st, st, st]
nest_of_values = ((st), ((st), (st)))
dict_of_values = {"foo": st, "bar": st, "baz": st}
self.assertEqual([st], nest.flatten(single_value))
self.assertEqual([[st, st, st]], nest.flatten(list_of_values))
self.assertEqual([st, st, st], nest.flatten(nest_of_values))
self.assertEqual([st, st, st], nest.flatten(dict_of_values))
