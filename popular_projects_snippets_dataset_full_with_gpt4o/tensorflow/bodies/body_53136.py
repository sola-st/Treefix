# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/proto_test.py
# create a constant of size > 64MB.
a = constant_op.constant(np.zeros([1024, 1024, 17]))
# Serialize the resulting graph def.
gdef = a.op.graph.as_graph_def()
serialized = gdef.SerializeToString()
unserialized = ops.Graph().as_graph_def()
# Deserialize back. Protobuf python library should support
# protos larger than 64MB.
unserialized.ParseFromString(serialized)
self.assertProtoEquals(unserialized, gdef)
