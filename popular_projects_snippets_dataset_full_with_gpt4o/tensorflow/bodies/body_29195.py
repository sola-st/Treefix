# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest_test.py
rt = ragged_factory_ops.constant_value([[[0]], [[1]]])
single_value = rt
list_of_values = [rt, rt, rt]
nest_of_values = ((rt), ((rt), (rt)))
dict_of_values = {"foo": rt, "bar": rt, "baz": rt}
self.assertEqual([rt], nest.flatten(single_value))
self.assertEqual([[rt, rt, rt]], nest.flatten(list_of_values))
self.assertEqual([rt, rt, rt], nest.flatten(nest_of_values))
self.assertEqual([rt, rt, rt], nest.flatten(dict_of_values))
