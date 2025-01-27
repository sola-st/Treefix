# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
values = nest.map_structure(
    lambda x: self.evaluate(x) if tensor_util.is_tf_type(x) else x,
    actual)
self.assertAllEqual(values, expected)
