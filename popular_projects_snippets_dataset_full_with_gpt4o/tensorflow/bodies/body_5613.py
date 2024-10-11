# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
# to_proto and from_proto are not supported.
v = self.create_variable([1, 2])
with self.assertRaises(TypeError):
    v.to_proto()
with self.assertRaises(TypeError):
    v.from_proto(variable_def=None)
