# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
op = test_ops.int_attr().op
op._set_attr("foo", attr_value_pb2.AttrValue(i=2))
# TODO(skyewm): add node_def check
self.assertEqual(op.get_attr("foo"), 2)
